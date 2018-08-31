#!/usr/bin/python
""" Author: Peter Swanson
            pswanson@ucdavis.edu
    Description: Class to hold article information
    Version: Python 2.7 """

import requests
from bs4 import BeautifulSoup
import unicodedata

class Article(object):
    ''' Class to hold article information and fetch text '''

    def __init__(self, source, date, url, title):
        self.source = source.encode('utf-8')
        self.url = url.encode('utf-8')
        self.title = title.encode('utf-8')
        self.date = str(date.tm_mon) + "-" + str(date.tm_mday) + "-" +  str(date.tm_year)
        

    def get_text(self):
        ''' Parse text from story based on a stored url '''

        # Get the page HTML
        page_html = requests.get(self.url).text

        # Parse the page with bs4
        page = BeautifulSoup(page_html, 'html.parser')
        
        # Remove Javascript
        for script in page(["script", "style"]):
            script.decompose()

        text = page.get_text()

        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

       # Thanks to Hugh Bothwell
       # https://stackoverflow.com/questions/22799990/beatifulsoup4-get-text-still-has-javascript
        
        return text

    def __str__(self):
        return  "\n" + " ----------- Article ----------- \n" + \
        "Source: " + self.source + "\nTitle: " + self.title + \
        "\nDate: " + self.date + "\nURL: " + self.url + \
        "\n ------------------------------- "

    def __repr__(self):
        return "<Article: " + self.title + ">"