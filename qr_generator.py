
"""
QR Code Generator

This application accepts a website URL from the user,
validates the URL, generates a QR code, and saves it
as a PNG image in the project directory.
"""

from pathlib import Path
from urllib.parse import urlsplit

import qrcode


# Define the location of the generated QR code image.
OUTPUT_FILE = Path(__file__).resolve().parent / "generated_qr.png"


def validate_url(user_input: str) -> str:
    """
    Validate the URL entered by the user.

    Add HTTPS when the protocol is not provided.
    Accept only valid HTTP and HTTPS URLs.

    Args:
        user_input: Website URL entered by the user.

    Returns:
        A validated URL string.

    Raises:
        ValueError: If the URL is empty or invalid.
    """

    url = user_input.strip()

    if not url:
        raise ValueError("URL cannot be empty.")

    # Add HTTPS if the user enters a domain without a protocol.
    if "://" not in url:
        url = f"https://{url}"

    # Reject whitespace in the URL.
    if any(character.isspace() for character in url):
        raise ValueError("URL must not contain spaces.")

    try:
        parsed_url = urlsplit(url)

        # Accessing the port also detects invalid port numbers.
        _ = parsed_url.port

    except ValueError as error:
        raise ValueError("Please enter a valid website URL.") from error

    # Validate the protocol and hostname.
    if (
        parsed_url.scheme not in ("http", "https")
        or not parsed_url.hostname
    ):
        raise ValueError(
            "Please enter a valid HTTP or HTTPS website URL."
        )

    # Check for malformed hostnames.
    hostname = parsed_url.hostname

    if (
        hostname.startswith(".")
        or hostname.endswith(".")
        or ".." in hostname
        or "/" in hostname
    ):
        raise ValueError("Please enter a valid website hostname.")

    return url


def generate_qr_code(url: str) -> None:
    """
    Generate a QR code for the supplied URL and save it as a PNG image.

    Args:
        url: Validated website URL to encode.

    Raises:
        qrcode.exceptions.DataOverflowError: If the data is too large.
        OSError: If the image cannot be saved.
    """

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    # Add the URL and automatically select a suitable QR code size.
    qr.add_data(url)
    qr.make(fit=True)

    # Generate a black-and-white QR code image.
    image = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    # Save the generated QR code in the project directory.
    image.save(OUTPUT_FILE)


def main() -> None:
    """Execute the QR code generator application."""

    print("\n================================")
    print("       QR CODE GENERATOR")
    print("================================")
    print("Enter a website URL to generate its QR code.")
    print("Example: https://www.bioxsystems.com/\n")

    try:
        user_input = input("Enter URL: ")

        # Validate the user-provided URL.
        url = validate_url(user_input)

        # Generate and save the QR code.
        generate_qr_code(url)

        print("\nQR code generated successfully!")
        print(f"Website URL : {url}")
        print(f"Output file : {OUTPUT_FILE}")

    except ValueError as error:
        print(f"\nInput Error: {error}")

    except qrcode.exceptions.DataOverflowError:
        print("\nError: The entered URL is too long for a QR code.")

    except OSError as error:
        print(f"\nFile Error: Unable to save the QR code. {error}")


if __name__ == "__main__":
    main()
