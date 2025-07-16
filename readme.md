# varzesh3 link downloader
This project is a simple Python script that scrapes non-video news links from the homepage's main list of the [Varzesh3](gttps://varzesh3.com) sports news website and saves them to a text file.
## requirements
- +python 3.7
- requests library
- beautifulsoup4 library
## installation
- create an empty folder in VSCode
- open terminal
- enter cmd
- create virtual venv use `python -m venv .venv`
- activate venv by `.venv\srcripts\activate`
- install requests library `pip install requests`
- install bs4 library `pip install BeautifulSoup`
- Copy the `varzesh3.py` into your project folder
## How to use
Run the News Link Scrape python `varzesh3.py`
(This will generate varzesh3_links.txt with all news article URLs.)

this script will:
1. Fetch the list page

2. Parse the HTML and extract all article links

3. Save the links to a file called linkss.txt
