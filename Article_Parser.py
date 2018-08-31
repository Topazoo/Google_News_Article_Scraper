#!/usr/bin/python
""" Author: Peter Swanson
            pswanson@ucdavis.edu
    Description: Class to parse article information
    
    Thanks to Hugh Bothwell
    https://stackoverflow.com/questions/22799990/beatifulsoup4-get-text-still-has-javascript
   
    Version: Python 2.7 """

import re
from bs4 import BeautifulSoup

class Article_Parser(object):
    ''' Takes an article in HTML and cleans unwanted content '''

    def __init__(self, article_html=None):
        if article_html:
            self.html = BeautifulSoup(article_html, 'html.parser')
        else:
            self.html = None

    def remove_js(self, page):
        ''' Remove javascript '''

        for script in page(["script", "style"]):
            script.decompose()
        for noscript in page(["noscript", "style"]):
            noscript.decompose()

    def remove_hd(self, page):
        ''' Remove header '''
        
        for header in page(["head", "class"]):
            header.decompose()
        for header in page(["head", "style"]):
            header.decompose()
        for header in page(["header", "class"]):
            header.decompose()
        for header in page(["header", "style"]):
            header.decompose()

    def remove_ft(self, page):
        ''' Remove footer '''

        for footer in page.select('div[class*="footer"]'):
            footer.decompose()
        for footer in page(["footer", "style"]):
            footer.decompose()

    def remove_lb(self, page):
        ''' Remove labels '''
       
        for label in page(["label", "style"]):
            label.decompose()

    def remove_bt(self, page):
        ''' Remove buttons '''
        
        for button in page(["button", "style"]):
            button.decompose()

    def remove_nv(self, page):
        ''' Remove navbar '''

        for nav in page(["nav", "style"]):
            nav.decompose()
        for nav in page(["navbar", "style"]):
            nav.decompose()
        for nav in page(["nav", "class"]):
            nav.decompose()
        for nav in page(["navbar", "class"]):
            nav.decompose()

    def remove_li(self, page):
        ''' Remove lists '''

        for li in page(["li", "style"]):
            li.decompose()

    def remove_sb(self, page):
        ''' Remove sidebar '''
        
        for sb in page.find_all("div", attrs={"class": re.compile("^sidebar*")}):
            sb.decompose()

    def remove_ad(self, page):
        ''' Remove ads ''' 

        for ad in page.find_all("div", attrs={"class": "component"}):
            ad.decompose()

    def format_html(self, page):
        ''' Final formatting for the HTML '''

        text = page.get_text()

        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        return text

    def parse_HTML(self, html=None):
        ''' Remove unwanted chunks of article HTML '''

        # Exit if no article html
        if self.html is None and html is None:
            print "Error - No article HTML given"
            exit(1)

        # If article html was given on instantiation
        elif self.html is not None and html is None:
            html = self.html

        else:
           html = BeautifulSoup(html, 'html.parser')

        # Remove unwanted comtent
        self.remove_js(html) # Javascript
        self.remove_ad(html) # Ads
        self.remove_hd(html) # Headers
        self.remove_nv(html) # Navbars
        self.remove_sb(html) # Sidebars
        self.remove_ft(html) # Footers
        self.remove_bt(html) # Buttons
        self.remove_lb(html) # Labels
        self.remove_li(html) # List Items

        # Perform final formatting and get text
        text = self.format_html(html)

        return text
        
