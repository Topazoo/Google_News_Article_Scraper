#!/usr/bin/python
""" Author: Peter Swanson
            pswanson@ucdavis.edu
    Description: Class to hold article information
    Version: Python 2.7 """

import requests
from Article_Parser import Article_Parser

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
        
        # Use parser to parse content
        parser = Article_Parser(page_html)
        parsed_page = parser.parse_HTML()

        return parsed_page

    def __str__(self):
        return  "\n" + " ----------- Article ----------- \n" + \
        "Source: " + self.source + "\nTitle: " + self.title + \
        "\nDate: " + self.date + "\nURL: " + self.url + \
        "\n ------------------------------- "

    def __repr__(self):
        return "<Article: " + self.title + ">"