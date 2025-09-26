######
## Justification cyber_capability
######

from typing import Any, Callable

from jpipe_runner.framework.decorators.jpipe_decorator import jpipe

## Strategy verify_ctf_cap_acceptable
@jpipe(consume=["test1", "test2", "test3", "test4", "test6"], produce=["test5"])
def verify_ctf_challenges_capability_is_acceptable(
        test1: str,
        test2: str,
        test3: str,
        test4: str,
        test6: str,
        produce: Callable[[str, Any], None]
    ) -> bool:
    print(test1, test2, test3, test4, test6)
    produce("test5", "test5")
    return True

## Evidence headlesslinux_distro
@jpipe(produce=["test6"])
def headless_linux_distribution_used_for_ctf(produce: Callable[[str, Any], None]) -> bool:
    produce("test6", "test6")
    return True

## Strategy verify_adversfine_cap_cybersec_acceptable
@jpipe(consume=["test5"])
def aggregate_all_the_models_evaluations_in_terms_of_cybersecurity_capabilities(test5: str) -> bool:
    print(test5)
    return True

## Evidence curated_ctf_challenges_list
@jpipe(produce=["test2"])
def curated_ctf_challenges_list(produce: Callable[[str, Any], None]) -> bool:
    produce("test2", "test2")
    return True

## Evidence ctf_eval_results
@jpipe(consume=[], produce=["test3"])
def ctf_challenges_evaluation_results(produce: Callable[[str, Any], None]) -> bool:
    produce("test3", "test3")
    return True

## Conclusion adversfine_cap_cybersec_acceptable
@jpipe(consume=["test5"])
def adversarially_finetuned_models_capability_in_cybersecurity_is_acceptable(test5: str) -> bool:
    print(test5)
    return True

## Evidence threshold_for_model_ctf_performance
@jpipe(consume=[], produce=["test4"])
def threshold_for_ctf_model_performance(produce: Callable[[str, Any], None]) -> bool:
    produce("test4", "test4")
    return True