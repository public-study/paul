from urllib.parse import urlsplit

from validator_interface import ValidatorInterface


class HasWWWValidator(ValidatorInterface):
    error_message = "Url has no 'www' prefix."

    @staticmethod
    def _is_valid(url: str) -> bool:
        return urlsplit(url).hostname.split(".")[0] == "www"
