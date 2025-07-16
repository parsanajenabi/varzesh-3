# varzesh3 link downloader
This project is a Python script that scrapes non-video news links from the homepage of the Varzesh3 sports news website and saves them to a text file.
## requirements
- +python 3.7
- telegram bot token
## installation
- create an empty folder in VSCode
- open terminal
- enter cmd
- create virtual venv use `python -m venv .venv`
- activate venv by `.venv\srcripts\activate`
- install requests library `pip install requests`
- install bs4 library `pip install BeautifulSoup`
## How to use
- Run the News Link Scrape python scrape_varzesh3.py
(This will generate varzesh3_links.txt with all news article URLs.)