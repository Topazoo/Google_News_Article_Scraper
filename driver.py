#!/usr/bin/python

""" Author: Peter Swanson
            pswanson@ucdavis.edu
    Description: Driver to collect and parse articles
    Version: Python 2.7 """

import sys
from Article_Collector import Article_Collector

def print_article_data(article):
    ''' Prints article info and text '''

    # String representation of article pretty-prints data
    print str(article)


    print ""

    # Fetch text on demand
    print article.get_text()

# A list of queries to search Google News
queries = ["Fortune", "Seeking Alpha"]
article_number = 0

# Get optional CLA - index of article to view
if len(sys.argv) > 1:
    article_number = int(sys.argv[1])

# Instantiate a collector with the queries
collector = Article_Collector(queries)

# Collect the article URLs
articles = collector.get_articles()
# Get article subject and text
collector.get_article_info(articles)

# Demo print first article or CLA input article index
print_article_data(articles[article_number])

