from pathlib import Path
import json

from jpipe_runner.framework.decorators.jpipe_decorator import jpipe


## Conclusion: Can be shared
@jpipe(consume=["is_linear_execution_order", "is_pep8_compliant", "are_quality_gates_met"])
def notebook_can_be_shared(is_linear_execution_order: bool, is_pep8_compliant: bool, are_quality_gates_met: bool) -> bool:
    return is_linear_execution_order and is_pep8_compliant and are_quality_gates_met


## Strategy: Linear execution order
@jpipe(consume=["notebook_file_path"], produce=["is_linear_execution_order"])
def verify_linear_execution_order(produce, notebook_file_path: str) -> bool:
    try:
        with open(notebook_file_path, "r", encoding="utf-8") as notebook_file:
            notebook = json.load(notebook_file)

        execution_counts = []
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") == "code":
                execution_count = cell.get("execution_count")
                if execution_count is not None:
                    execution_counts.append(execution_count)

        is_linear_order = execution_counts == sorted(execution_counts)
    except Exception:
        is_linear_order = False

    produce("is_linear_execution_order", is_linear_order)
    return is_linear_order


## Strategy: PEP8 compliance (basic line length + indentation check)
@jpipe(consume=["notebook_file_path"], produce=["is_pep8_compliant"])
def check_pep8_compliance(produce, notebook_file_path: str) -> bool:
    try:
        with open(notebook_file_path, "r", encoding="utf-8") as notebook_file:
            notebook = json.load(notebook_file)

        is_compliant = True
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") == "code":
                for line in cell.get("source", []):
                    if len(line) > 79 or (line.startswith(" ") and (len(line) - len(line.lstrip())) % 4 != 0):
                        is_compliant = False
                        break
            if not is_compliant:
                break
    except Exception:
        is_compliant = False

    produce("is_pep8_compliant", is_compliant)
    return is_compliant


## Strategy: Gate check
@jpipe(consume=["is_pep8_compliant", "is_linear_execution_order"], produce=["are_quality_gates_met"])
def check_quality_gates(produce, is_pep8_compliant: bool, is_linear_execution_order: bool) -> bool:
    quality_gates_met = is_pep8_compliant and is_linear_execution_order
    produce("are_quality_gates_met", quality_gates_met)
    return quality_gates_met


## Evidence: Notebook file exists
@jpipe(consume=["notebook_path"], produce=["notebook_file_path"])
def check_notebook_exists(notebook_path: str, produce) -> bool:
    notebook_file_exists = Path(notebook_path).is_file()
    produce("notebook_file_path", notebook_path)
    return notebook_file_exists
