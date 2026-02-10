# Cross-Browser Testing Tool

This Python project uses Selenium WebDriver to test a given URL across multiple browsers (Chrome, Firefox, Edge) in headless mode.

## Installation

1. Install Python (if not already installed).
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script with a URL as argument:

```
python main.py https://example.com
```

The script will:
- Open the URL in Chrome, Firefox, and Edge browsers in headless mode.
- Take screenshots for each browser.
- Save screenshots as `screenshot_chrome.png`, `screenshot_firefox.png`, `screenshot_edge.png`.

If any browser fails to load the page, it will print an error message.

## Requirements

- Python 3.x
- Internet connection (for downloading browser drivers)
- Browsers: Chrome, Firefox, Edge must be installed on the system