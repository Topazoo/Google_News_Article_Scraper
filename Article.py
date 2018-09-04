#!/usr/bin/python
""" Author: Peter Swanson
            pswanson@ucdavis.edu
    Description: Class to hold article information
    Version: Python 2.7 """

import requests
from collections import Counter
from Article_Parser import Article_Parser
from nltk.tag import pos_tag

class Article(object):
    ''' Class to hold article information and fetch text '''

    def __init__(self, source, date, url, title):
        self.source = source.encode('utf-8')
        self.url = url.encode('utf-8')
        self.title = title.encode('utf-8')
        self.date = str(date.tm_mon) + "-" + str(date.tm_mday) + "-" +  str(date.tm_year)

        self.text = None
        self.subject = None

    def find_subject(self, breadth=7):
        ''' Attempt to determine the subject of an article '''
        
        # Get proper nouns from title and text 
        title_nouns = self.get_keywords(self.title)
        article_nouns = self.get_keywords(self.get_text())

        # Count proper nouns in article        
        article_counter = Counter(article_nouns)

        # Subject if keywords from title appear often
        for noun in title_nouns:
            for art_noun in article_counter.most_common(breadth):
                if noun == art_noun[0]:
                    self.subject = noun
                    return noun

        return None

    def get_keywords(self, text):
        ''' Get and return a list of proper nouns from article '''

        # Split and tag text
        tagged_text = pos_tag(text.split())

        # Take only proper nouns
        key_words = [word for word,pos in tagged_text if pos == 'NNP']
        sanatized_kw = []

        # Remove apostrophies and plurals
        for word in key_words:
            try:
                word = word.replace(u"\u2019", '\'')
            except UnicodeDecodeError:
                word = word.decode("utf-8", "ignore").replace(u"\u2019", '\'')

            if '\'s' in word:
                word = word[:-2:]
            if '\'' in word:
                word = word[:-1:]

            sanatized_kw.append(word)

        return sanatized_kw

    def get_text(self):
        ''' Parse text from story based on a stored url '''

        if not self.text:
            # Get the page HTML
            page_html = requests.get(self.url).text
            
            # Use parser to parse content
            parser = Article_Parser(page_html)
            parsed_page = parser.parse_HTML()

            self.text = parsed_page
            return parsed_page
        else:
            return self.text

    def __str__(self):
        return  "\n" + " ----------- Article ----------- \n" + \
        "Source: " + self.source + "\nTitle: " + self.title + \
        "\nSubject: " + str(self.subject) + \
        "\nDate: " + self.date + "\nURL: " + self.url + \
        "\n ------------------------------- "

    def __repr__(self):
        return "<Article: " + self.title + ">"