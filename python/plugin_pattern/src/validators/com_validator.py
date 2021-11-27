from urllib.parse import urlsplit

from validator_interface import ValidatorInterface


class ComValidator(ValidatorInterface):
    error_message = "Url does not have a 'com' domain."

    @staticmethod
    def _is_valid(url: str) -> bool:
        return urlsplit(url).netloc.split(".")[-1] == "com"
