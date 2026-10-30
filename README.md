# QR-Code-Generator

## Overview

This project is a simple QR Code Generator developed
using Python.

The application accepts a website URL from the user,
validates the entered address, and generates a QR code
image using the Python qrcode library.

The generated QR code is saved as `generated_qr.png`
in the project directory.

## Requirements

- Python 3
- qrcode library
- Pillow library (for image generation)

## Project Structure

```text
qr_code_generator/
│
├── qr_generator.py
├── requirements.txt
├── README.md
└── generated_qr.png
```

## Setup Instructions

1. Clone or download the project.
2. Open the project directory in Terminal.
3. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

4. Activate the virtual environment:

   ```bash
   source .venv/bin/activate
   ```

5. Install the required packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Compile and Run

Python is an interpreted language, so a separate
compilation step is not required.

To check the Python source code for syntax errors:

```bash
python -m py_compile qr_generator.py
```

To run the application:

```bash
python qr_generator.py
```

Enter a website URL when prompted.

Example:

```text
https://www.bioxsystems.com/
```

## Output

The application generates a QR code image named:

`generated_qr.png`

The image is saved in the project directory.

Scan the generated QR code using a mobile phone
camera to access the encoded website.

## Dependencies

All required Python packages are listed in
`requirements.txt`.

Install them using:

```bash
python -m pip install -r requirements.txt
```
