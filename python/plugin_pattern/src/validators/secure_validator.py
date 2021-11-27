from urllib.parse import urlsplit

from validator_interface import Priority, ValidatorInterface


class SecureValidator(ValidatorInterface):
    error_message = "Url is not secure."
    priority = Priority.HIGH

    @staticmethod
    def _is_valid(url: str) -> bool:
        return urlsplit(url).scheme == "https"
