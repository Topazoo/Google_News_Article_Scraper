#!/usr/bin/python
""" Author: Peter Swanson
            pswanson@ucdavis.edu
    Description: Class to collect article information
    Version: Python 2.7 """

import feedparser
from Article import Article       

class Article_Collector(object):
    ''' Class to collect articles from Google RSS feeds '''

    url_first_chunk = "https://news.google.com/news/rss/search/section/q/"
    url_last_chunk = "?ned=us&gl=US&hl=en"

    def __init__(self, query_list = None):
        self.query_list = query_list

    def format_queries(self, query_list):
        ''' Format queries and return dict of full Google RSS urls '''

        url_query_dict = {}

        for query in query_list:
            # Spaces become '+' signs
            query_sp_rplc = str(query).replace(" ", "+")
            # Build full url
            full_url = self.url_first_chunk + query_sp_rplc + self.url_last_chunk
            # Add to list
            url_query_dict[query] = full_url

        return url_query_dict

    def parse_feeds(self, url_dict):
        ''' Get RSS feed for every query from created URL '''

        article_list = []

        # For every query
        for query, url in url_dict.items():
            # Get a feed of news articles from Google 
            feed = feedparser.parse(url)

            # Make a list of Articles
            for entry in feed.entries:
                article = Article(query, entry.published_parsed, entry.link, entry.title)
                article_list.append(article)

        return article_list

    def get_articles(self, query_list = None):
        ''' Get articles from passed list of search terms '''

        # Exit if no list
        if self.query_list is None and query_list is None:
            print "Error - No query list given"
            exit(1)

        # If list was given on instantiation
        elif self.query_list is not None and query_list is None:
            query_list = self.query_list
        
        # Get urls for Google RSS feeds for each query
        feed_urls_dict = self.format_queries(query_list)

        # Collect articles from each feed
        articles = self.parse_feeds(feed_urls_dict)

        return articles




