from src import services


URLS = [
    "http://some.url/",
    "https://www.url-without-errors.com/"
]


def main() -> None:
    """
    For each url runs a series of validations.
    Sends an email with occurred errors.
    """
    for url in URLS:
        errors = services.validate_url(url)
        message = services.construct_message(url, errors)
        services.send_email(message)


if __name__ == "__main__":
    main()
