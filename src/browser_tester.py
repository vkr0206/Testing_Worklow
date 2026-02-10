"""
Browser testing module for cross-browser testing.
"""
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


class BrowserTester:
    """Test URLs across multiple browsers."""
    
    SUPPORTED_BROWSERS = ['chrome', 'firefox', 'edge']
    
    @staticmethod
    def test_url_in_browser(url: str, browser_name: str) -> bool:
        """
        Test a URL in the specified browser.
        
        Args:
            url: URL to test
            browser_name: Browser name ('chrome', 'firefox', 'edge')
            
        Returns:
            bool: True if test passed, False otherwise
        """
        try:
            if browser_name == 'chrome':
                options = ChromeOptions()
                options.add_argument('--headless')
                driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install()),
                    options=options
                )
            elif browser_name == 'firefox':
                options = FirefoxOptions()
                options.add_argument('--headless')
                driver = webdriver.Firefox(
                    service=FirefoxService(GeckoDriverManager().install()),
                    options=options
                )
            elif browser_name == 'edge':
                options = EdgeOptions()
                options.add_argument('--headless')
                driver = webdriver.Edge(
                    service=EdgeService(EdgeChromiumDriverManager().install()),
                    options=options
                )
            else:
                raise ValueError(f"Unsupported browser: {browser_name}")

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

    @staticmethod
    def test_all_browsers(url: str) -> dict:
        """
        Test URL in all supported browsers.
        
        Args:
            url: URL to test
            
        Returns:
            dict: Results for each browser
        """
        results = {}
        for browser in BrowserTester.SUPPORTED_BROWSERS:
            results[browser] = BrowserTester.test_url_in_browser(url, browser)
        return results
