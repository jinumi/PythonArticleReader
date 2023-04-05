# Article Reader

This is a Python script that can read the text content of an article aloud using text-to-speech technology.

## Requirements

    * Python 3
    * Requests library (pip install requests)
    * Beautiful Soup 4 library (pip install beautifulsoup4)
    * Pyttsx3 library (pip install pyttsx3)

## Usage

To use the script, simply run the article_reader.py file and enter the URL of the article when prompted. The script will then read the text content of the article aloud using the default system text-to-speech engine.

## Troubleshooting

If the script fails to read the article aloud or produces an error, make sure that the article is accessible at the specified URL and that the required libraries are installed correctly.
If the article does not contain a clear <article> tag, the script may fail to read the correct content. In this case, you may need to modify the script to use a different method for identifying the article content.

## License

This project is licensed under the MIT License.
