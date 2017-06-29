# PYTHON SELENIUM BASIC

## Setup (this assumes that you already have Python and pip installed)

- If you clone this repo, you can do `pip install -r requirements.txt` to install the prerequisite python libraries

Note: requirements.txt does not include webdrivers e.g geckodriver, chromedriver, etc. since 
selenium 3 does not include a standalone geckodriver for Firefox.

## Installing webdrivers for unix

### geckodriver

- Download tar file from [geckodriver](https://github.com/mozilla/geckodriver/releases)
- Go to download location and extract the file:
```
tar -xvzf geckodriver
```
- Make geckodriver executable:
```
chmod +x geckodriver
```
- Add geckodriver executable to your `PATH`. For testing purposes
you can just
```
export PATH=$PATH:[directory of where the driver/s are located]
```
or just make sure the drivers are located your PATH, e. g., place it in /usr/bin or /usr/local/bin.
otherwise you may encounter error upon running selenium
`selenium.common.exceptions.WebDriverException: Message: ‘geckodriver’ executable needs to be in PATH.`

## How to run the app
`python app.py`