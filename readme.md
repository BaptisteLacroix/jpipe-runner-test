# jpipe-runner-test

## Overview

This repository is designed to test and validate new features added to the jpipe runner versions. It serves as a comprehensive testing environment for the jpipe pipeline functionality, particularly focusing on:

- Pipeline execution validation
- GitHub bot integration for pull request comments
- Automated justification diagram generation
- Error reporting and status feedback

## Key Features Being Tested

### 1. Pipeline Execution
The repository tests the core jpipe runner functionality using a sample notebook quality justification pipeline.

### 2. GitHub Bot Integration
When pull requests are created, the GitHub Actions workflow automatically:
- Executes the jpipe pipeline
- Generates justification diagrams
- Posts detailed comments with execution results
- Provides downloadable artifacts

### 3. Automated Feedback
The bot provides comprehensive feedback including:
- **Success scenarios**: Diagram images and execution summaries
- **Failure scenarios**: Detailed error messages and debugging information

## Repository Structure

```
├── .github/
│   └── workflows/
│       └── workflow.yaml          # GitHub Actions workflow configuration
├── config.yaml                    # jpipe runner configuration
├── expected_diagram.png           # Reference diagram for validation
├── justification.jd.json          # Justification definition file
├── notebook_hello_world.ipynb     # Sample notebook for testing
├── steps.py                       # Pipeline step definitions
└── readme.md                      # This file
```

## Getting Started

### Prerequisites

- Python 3.11+
- jpipe-runner (installed via GitHub Actions or manually)
- Access to GitHub repository with appropriate permissions

### Local Testing

To test the pipeline locally, run:

```sh
jpipe-runner -l 'steps.py' --config-file 'config.yaml' 'justification.jd.json' --format svg -o .
```

### Expected Local Output

```text
==============================================================================
jPipe Files
==============================================================================
jPipe Files.Justification :: notebook_quality
==============================================================================
evidence<notebook> :: notebook file exists                            | PASS |
------------------------------------------------------------------------------
strategy<linear> :: Verify notebook has linear execution order        | PASS |
------------------------------------------------------------------------------
strategy<pep8> :: Check PEP8 coding standard                          | PASS |
------------------------------------------------------------------------------
sub-conclusion<repro> :: Execution environment is reproducible        | PASS |
------------------------------------------------------------------------------
sub-conclusion<fair> :: Notebook code quality is fair                 | PASS |
------------------------------------------------------------------------------
strategy<gate> :: Assess quality gates are met                        | PASS |
------------------------------------------------------------------------------
conclusion<shareable> :: Notebook can be shared                       | PASS |
------------------------------------------------------------------------------
jPipe Files
1 justification, 7 passed, 0 failed, 0 skipped
==============================================================================
png diagram saved to: diagram.png
```

### Expected Diagram Output

![Expected Diagram Output](expected_diagram.png)

## Testing Workflow

### Automated Testing via Pull Requests

1. **Create a Pull Request**: Any PR will trigger the GitHub Actions workflow
2. **Pipeline Execution**: The workflow runs the jpipe runner with the configured parameters
3. **Results**: The bot comments on the PR with execution results

### Example Bot Comments

#### Successful Execution
> Justification process completed successfully!
> </detail>


#### Failed Execution

> Justification process failed!
> 
> ![Generated Diagram](https://raw.githubusercontent.com/.../diagram.svg)
> 
> [Download Diagram Artifact](https://github.com/.../artifacts/...)
> 
> <details><summary>Runner Output</summary>
> 
> ```
> ERROR - validate():297 - 2025-09-15 16:49:57,935 - > [MissingVariableValidator]
> Pipeline validation error: missing variable.
>   • Function 'check_notebook_exists' declares that it consumes variable 'notebook_path',
>     but no producer for this variable is found in the pipeline,
>     nor is it provided in the 'main' context.
>   • To fix:
>     - Ensure that some earlier function produces 'notebook_path', or
>     - Provide '{var}' via config/context,
>     so that 'check_notebook_exists' can consume it.
> ```
>
></details>

## Configuration

### GitHub Actions Workflow

The workflow is configured in `.github/workflows/workflow.yaml` and includes:

- **Python 3.13** setup
- **jpipe-runner** action with version `feat/v3.1.0`
- **Image embedding** to the `diagram-images` branch
- **Artifact generation** for downloadable diagrams

### jpipe Configuration

Key configuration parameters:
- **jd_file**: `justification.jd.json`
- **config-file**: `config.yaml`
- **library**: `steps.py`
- **embed_image**: `true`
- **image_branch**: `diagram-images`

## Development and Testing

### Adding New Test Cases

1. Modify `justification.jd.json` to include new justification scenarios
2. Update `steps.py` with corresponding step implementations
3. Adjust `config.yaml` for any new configuration requirements
4. Create a pull request to test the changes

### Debugging Failures

When the pipeline fails:
1. Check the bot comment for detailed error messages
2. Download the diagram artifact to see partial execution results
3. Review the full GitHub Actions logs for additional context
4. Test locally using the command provided above

## Expected Diagram

The pipeline generates a justification diagram showing the relationship between evidence, strategies, sub-conclusions, and final conclusions. You can compare generated diagrams with the reference image:

![Expected Diagram](expected_diagram.png)
