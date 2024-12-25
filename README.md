# Keylogger Project

This project is a simple keylogger implemented in Python that listens to keystrokes, identifies the active window/application, and sends the recorded keystrokes via email when the user presses the **ESC** key. The project is divided into multiple modules to handle different responsibilities.

## Table of Contents

- [Overview](#overview)
- [Modules](#modules)
  - [identify_operating_systems.py](#identify_operating_systemspy)
  - [keyboard_listener.py](#keyboard_listenerpy)
  - [send_mail.py](#send_mailpy)
  - [main.py](#mainpy)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview

This keylogger is designed to:
1. Identify the operating system and the active window/application.
2. Record the keystrokes made by the user.
3. Send the recorded data to a specified email address once the user presses the **ESC** key.

The project is modularized into different scripts to make it easy to manage and extend. It uses Python’s threading module to run the keystroke listener and active window tracker concurrently.

## Modules

### `identify_operating_systems.py`

This module is responsible for:
- Identifying the operating system on which the script is running.
- Based on the OS, it uses different methods to track the currently active application or window.

### `keyboard_listener.py`

This module listens for keystrokes from the user:
- It records the keystrokes and appends them to a log.
- It stops recording when the **ESC** key is pressed.

### `send_mail.py`

This module sends an email with the recorded keystrokes attached as a file:
- It connects to an SMTP server and sends the log file to a specified recipient address.
- The SMTP configuration can be modified as needed to match the email service you want to use.

### `main.py`

This is the entry point for the script, which:
- Creates and runs two threads:
  - One thread runs the keystroke listener.
  - The other runs the active window identification.
- Once the ESC key is pressed, the keystroke listener stops, the active window tracker stops running, and the email with the recorded keystrokes is sent.

---

## Requirements

- Python 3.x
- `pynput` library for keylogging
- `pygetwindow`, `pywin32`, `pyobjc`, or `Xlib` (depending on your OS) for identifying the active window
- `smtplib` for sending emails
- `email` library for email formatting

To install the required libraries, run:

```bash
pip install pynput pygetwindow pywin32 pyobjc xlib
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Dark5301/keystroke-logger.git
cd keystroke-logger
```
## Usage

1. Edit the **`send_mail.py`** file to configure the SMTP settings and recipient email address.
2. Run the **`main.py`** script:

```bash
python main.py
```

3. The script will start logging keystrokes and track the active window.
4. Press the **ESC** key to stop the keylogging and send the email with the recorded data.

Once the **ESC** key is pressed, the keystrokes along with the active window information will be logged to a file and emailed to the recipient configured in the `send_mail.py` script.

---

## Example Output

Once the script is running, it will log keystrokes along with the active window, like:

```
Chrome
h
e
l
l
o
Notepad
t
h
e
r
e
```

And upon stopping, it will email a file with the recorded data to the specified recipient.

---

## License

This project is for educational purposes only. Use it responsibly and ensure that it complies with applicable laws and regulations.

---

This `README.md` should provide a comprehensive overview of your project, its modules, installation, and usage instructions. Adjust any sections as needed for your specific implementation or further customization!
