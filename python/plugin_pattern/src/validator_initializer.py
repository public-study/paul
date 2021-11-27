import importlib.util
from collections import defaultdict
from inspect import getmembers, isclass
from pathlib import Path
import sys
from typing import Type

from .validators import validator_interface
from .validators.validator_interface import Priority, ValidatorInterface


VALIDATOR_PATTERN = "validators/*_validator.py"
_validators: list[Type[ValidatorInterface]] = []


def get_validators() -> list[Type[ValidatorInterface]]:
    """
    If not validators were loaded before, loads them in ordered manner,
    where validators with high priority are first in the list.
    """
    if not _validators:
        print("Loading validators for the first time.\n")
        unordered_validators = _get_unordered_validators()
        for _, validators_of_same_priority in sorted(unordered_validators.items()):
            _validators.extend(validators_of_same_priority)
    return _validators


def _get_unordered_validators() -> dict[Priority, list[ValidatorInterface]]:
    """
    Loads all validator classes from validator modules, which should match two rules:
        - Be inside validators package
        - Should be called <some_name>_validator.py
    Puts those validators into a dict, where keys are priorities,
    values are lists of validators of given priority.
    """
    result_validators = defaultdict(list)

    # Add validator_interface module into sys.modules,
    # so it can be loaded in separate validator modules
    validator_interface_name = Path(validator_interface.__file__).resolve().with_suffix("").name
    sys.modules[validator_interface_name] = validator_interface

    # Find all validators in validators package
    validator_module_paths_gen = Path(__file__).resolve().parent.glob(VALIDATOR_PATTERN)
    for validator_module_path in validator_module_paths_gen:
        # For each found validator, import the validator into memory
        spec = importlib.util.spec_from_file_location(
            validator_module_path.with_suffix("").name,
            validator_module_path
        )
        validator_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator_module)

        # Append all subclasses of ValidatorInterface to the validators list
        validator_classes = getmembers(validator_module, isclass)
        for _, validator in validator_classes:
            if issubclass(validator, ValidatorInterface) and validator is not ValidatorInterface:
                result_validators[validator.priority].append(validator)

    return result_validators
