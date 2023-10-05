# Clipboard Password Scrubber

## Description

Clipboard Password Scrubber is a simple yet effective Python script designed to keep your clipboard free from sensitive information like passwords. This script scans the clipboard and removes any data that matches the pattern of a password, ensuring that sensitive information is not left exposed.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Automation](#automation)
  - [Windows](#windows)
  - [macOS and Linux](#macos-and-linux)
- [Contribution](#contribution)
- [License](#license)

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/Clipboard-Password-Scrubber.git
    ```

2. Navigate to the project directory:

    ```
    cd Clipboard-Password-Scrubber
    ```

3. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

To run the script manually:

1. Navigate to the project directory.

2. Run the Python script:

    ```
    python clipboard_scrubber.py
    ```

## Automation

### Windows

#### Task Scheduler

1. Open Task Scheduler from the Windows search bar.

2. Go to `Action > Create Basic Task`.

3. Name your task "Clipboard Password Scrubber".

4. Set the Trigger to either `Daily` or `At startup`.

5. For Action, choose `Start a program`.

6. For `Program/script`, browse to your Python executable and add the script as an argument:

    ```
    Program/script: C:\Python39\python.exe
    Add arguments: C:\path\to\your\script.py
    ```

#### Batch File

1. Create a `.bat` file with the following content:

    ```batch
    @echo off
    :loop
    python C:\path\to\your\script.py
    timeout /t 60
    goto loop
    ```

2. Run the batch file or add it to your startup programs.

### macOS and Linux

#### Cron Job

1. Open Terminal.

2. Type `crontab -e`.

3. Add the following line to run the script every minute:

    ```cron
    * * * * * /usr/bin/python3 /path/to/your/script.py
    ```

#### Shell Script

1. Create a `.sh` file:

    ```sh
    #!/bin/bash
    while true; do
      python3 /path/to/your/script.py
      sleep 60
    done
    ```

2. Make it executable: `chmod +x /path/to/your/shellscript.sh`

3. Run the script: `./path/to/your/shellscript.sh`

## Contribution

Contributions are welcome! Create a pull request to propose and collaborate on changes.

## License

MIT License. See `LICENSE` for more information.
