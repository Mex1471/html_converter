# html_converter
Basic WebArchive to HTML

# WebArchive to HTML Converter

This is a simple Python script that allows you to convert WebArchive files (.webarchive) to HTML format. The script provides a GUI using Tkinter, enabling users to select multiple WebArchive files and specify an output directory for the converted HTML files.

## Features

- Select multiple WebArchive files for conversion.
- Choose an output directory to save the converted HTML files.
- Option to create a subfolder named "html converted" in the output directory.
- Double-click on a selected file to set the output directory to the parent directory of the file.

## Requirements

- Python 3.x
- `beautifulsoup4` library
- `lxml` library

## Installation

1. Install Python 3.x from the official [Python website](https://www.python.org/).
2. Install the required libraries:

    ```bash
    pip install beautifulsoup4 lxml
    ```

3. Ensure `tkinter` is installed on your system:
    - For Ubuntu/Debian:
        ```bash
        sudo apt-get update
        sudo apt-get install python3-tk
        ```
    - For Fedora:
        ```bash
        sudo dnf install python3-tkinter
        ```
    - For macOS (using Homebrew):
        ```bash
        brew install python-tk
        ```

## Usage

1. Clone or download this repository and navigate to the directory containing `converter_v0.1.py`.

2. Run the script:

    ```bash
    python3 converter_v0.1.py
    ```

3. A GUI window will appear. Follow these steps to convert your WebArchive files:

    - Click on "Select WebArchive Files" to choose the files you want to convert.
    - (Optional) Double-click on a selected file to set the output directory to the parent directory of the file.
    - Click on "Browse" to select the output directory where the converted HTML files will be saved.
    - (Optional) Check the "Create 'html converted' subfolder" checkbox if you want to save the converted files in a subfolder named "html converted".
    - Click on "Convert" to start the conversion process.

4. Once the conversion is complete, a message box will appear indicating the number of successfully converted files.

## Building an Executable

To create an executable file from this script, you can use `pyinstaller`. Follow these steps:

1. Install `pyinstaller`:

    ```bash
    pip install pyinstaller
    ```

2. Navigate to the directory containing `converter_v0.1.py`.

3. Run the following command to create an executable:

    - For Windows:

        ```bash
        pyinstaller --onefile --windowed converter_v0.1.py
        ```

    - For macOS:

        ```bash
        pyinstaller --onefile --windowed converter_v0.1.py
        ```

4. The executable will be created in the `dist` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The script uses the `beautifulsoup4` and `lxml` libraries for parsing HTML content.
- Tkinter is used for the graphical user interface.
