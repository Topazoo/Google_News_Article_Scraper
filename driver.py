#!/usr/bin/python
#!/usr/bin/python
""" Author: Peter Swanson
            pswanson@ucdavis.edu
    Description: Driver to collect and parse articles
    Version: Python 2.7 """

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

# Instantiate a collector with the queries
collector = Article_Collector(queries)

# Collect the article information
articles = collector.get_articles()

# Demo print first article
print_article_data(articles[0])

