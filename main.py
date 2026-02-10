import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def test_url_in_browser(url, browser_name):
    try:
        if browser_name == 'chrome':
            options = ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser_name == 'firefox':
            options = FirefoxOptions()
            options.add_argument('--headless')
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        elif browser_name == 'edge':
            options = EdgeOptions()
            options.add_argument('--headless')
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
        else:
            print(f"Unsupported browser: {browser_name}")
            return False

        driver.get(url)
        # Take screenshot
        screenshot_path = f"screenshot_{browser_name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Successfully tested {url} in {browser_name}. Screenshot saved as {screenshot_path}")
        driver.quit()
        return True
    except Exception as e:
        print(f"Error testing {url} in {browser_name}: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    browsers = ['chrome', 'firefox', 'edge']

    for browser in browsers:
        success = test_url_in_browser(url, browser)
        if not success:
            print(f"Failed to test in {browser}")