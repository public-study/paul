from .validator_initializer import get_validators


def validate_url(url: str) -> list[str]:
    errors = []
    for validator in get_validators():
        error = validator.validate(url)
        if error:
            errors.append(error)
        if validator.should_stop:
            break

    return errors


def send_email(message: str) -> None:
    print(message)


def construct_message(url: str, errors: list[str]) -> str:
    message_parts = [f"Results of validating of url {url}.\n"]
    if errors:
        message_parts.append("Some errors occurred during processing:")
        message_parts.extend(f"- {error}" for error in errors)
    else:
        message_parts.append("Validation run without any errors.")
    return "\n".join(message_parts) + "\n"
