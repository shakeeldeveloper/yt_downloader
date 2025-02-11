from setuptools import setup, find_packages

setup(
    name="yt_downloader",
    version="0.1",
    packages=find_packages(),
    install_requires=["pytube"],
    author="Muhammad Shakeel",
    author_email="shakeeldevelopers@gmail.com",
    description="A simple YouTube video downloader",
    url="https://github.com/yourusername/yt_downloader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
