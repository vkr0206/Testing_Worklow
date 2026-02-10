"""
Test cases for the BrowserTester module.
"""
import pytest
from unittest.mock import patch, MagicMock
from src.browser_tester import BrowserTester


class TestBrowserTester:
    """Test cases for BrowserTester class."""
    
    def test_supported_browsers(self):
        """Test that all expected browsers are in supported list."""
        assert 'chrome' in BrowserTester.SUPPORTED_BROWSERS
        assert 'firefox' in BrowserTester.SUPPORTED_BROWSERS
        assert 'edge' in BrowserTester.SUPPORTED_BROWSERS
    
    @patch('src.browser_tester.webdriver.Chrome')
    def test_test_url_in_chrome(self, mock_chrome):
        """Test URL testing in Chrome browser."""
        # Setup mock
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        
        # Test
        with patch('src.browser_tester.ChromeDriverManager'):
            with patch('src.browser_tester.ChromeService'):
                result = BrowserTester.test_url_in_browser('https://example.com', 'chrome')
        
        # Verify
        assert result is True
        mock_driver.get.assert_called_once_with('https://example.com')
        mock_driver.save_screenshot.assert_called_once()
        mock_driver.quit.assert_called_once()
    
    @patch('src.browser_tester.webdriver.Firefox')
    def test_test_url_in_firefox(self, mock_firefox):
        """Test URL testing in Firefox browser."""
        # Setup mock
        mock_driver = MagicMock()
        mock_firefox.return_value = mock_driver
        
        # Test
        with patch('src.browser_tester.GeckoDriverManager'):
            with patch('src.browser_tester.FirefoxService'):
                result = BrowserTester.test_url_in_browser('https://example.com', 'firefox')
        
        # Verify
        assert result is True
        mock_driver.quit.assert_called_once()
    
    def test_test_url_with_invalid_browser(self):
        """Test that invalid browser raises error."""
        with pytest.raises(ValueError, match="Unsupported browser"):
            BrowserTester.test_url_in_browser('https://example.com', 'safari')
    
    @patch('src.browser_tester.BrowserTester.test_url_in_browser')
    def test_test_all_browsers(self, mock_test):
        """Test testing all browsers."""
        # Setup mock to return True for all browsers
        mock_test.return_value = True
        
        # Test
        results = BrowserTester.test_all_browsers('https://example.com')
        
        # Verify
        assert len(results) == 3
        assert all(result is True for result in results.values())
        assert mock_test.call_count == 3
