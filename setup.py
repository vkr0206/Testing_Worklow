"""
Setup configuration for the Python testing project.
"""
from setuptools import setup, find_packages

setup(
    name="browser-test-suite",
    version="1.0.0",
    description="Cross-browser testing tool using Selenium",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "selenium>=4.0.0",
        "webdriver-manager>=3.8.0",
    ],
    extras_require={
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-mock>=3.10.0",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)
