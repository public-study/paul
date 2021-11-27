from abc import ABC, abstractmethod
from enum import IntEnum
from typing import Optional


class Priority(IntEnum):
    HIGH = 0
    MEDIUM = 1
    LOW = 2


class ValidatorInterface(ABC):
    should_stop: bool = False
    error_message: Optional[str] = None
    priority: Priority = Priority.LOW

    @classmethod
    def validate(cls, url: str) -> str:
        if not cls._is_valid(url):
            return cls._get_error_message()
        return ""

    @staticmethod
    @abstractmethod
    def _is_valid(url: str) -> bool:
        pass

    @classmethod
    def _get_error_message(cls):
        if cls.error_message is None:
            raise AttributeError(f"error_message should be filled in {cls.__name__}")
        return cls.error_message

