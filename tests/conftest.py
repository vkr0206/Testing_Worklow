"""
Pytest configuration and fixtures.
"""
import pytest


@pytest.fixture
def sample_url():
    """Provide a sample URL for testing."""
    return 'https://example.com'


@pytest.fixture
def supported_browsers():
    """Provide list of supported browsers."""
    return ['chrome', 'firefox', 'edge']
