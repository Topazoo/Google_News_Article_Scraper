# Google News Article Scraper
### Author: Peter Swanson
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 2.7](https://img.shields.io/badge/Python-2.7-brightgreen.svg)](https://www.python.org/downloads/release/python-2714/)
[![requests 2.19.1](https://img.shields.io/badge/requests-2.19.1-brightgreen.svg)](https://pypi.org/project/requests/)
[![beautifulsoup4 4.6.3](https://img.shields.io/badge/beautifulsoup4-4.6.3-brightgreen.svg)](https://pypi.org/project/beautifulsoup4/)
[![feedparser 5.2.1](https://img.shields.io/badge/feedparser-5.2.1-brightgreen.svg)](https://pypi.org/project/feedparser/)
[![nltk 3.3](https://img.shields.io/badge/nltk-3.3-brightgreen.svg)](https://pypi.org/project/nltk/)

## Background:
Online news articles are incredibly valuable to data scientists seeking to understand long-term trends.
One of the most difficult parts of analyzing these articles is parsing them. 
Online news articles collected via script must be parsed from the HTML of the page they are hosted on. 

<b>This application makes collecting and parsing stories from Google News incredibly easy!</b>

This repository contains the Python code for collecting and parsing articles, as well as a sample driver.

## Running the Application:
### Installing Dependencies:
Ensure the following are installed on the machine you are running the application on:
- Python 2.7 with pip
- virtualenv for Python 2.7

Create a virtualenv and install the requirements from <i>requirements.txt</i> with pip
```
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r "requirements.txt"
``` 

### Running the Driver:
The driver can be run with Python:
```
(venv) $ python driver.py
```

By default, the driver collects articles based on the queries "Fortune" and "Seeking Alpha", then
prints the parsed text of the first article.

The driver can be run with an optional command line argument to view an article at a specific index.
```
(venv) $ python driver.py 3
```

### Collecting Articles:
The article collector can be used from Python code or the console if imported.
It can be instantiated with a list of queries or given a list of queries later on.

#### Instantiation:
```
>>> queries = ["Tesla"]
>>> from Article_Collector import Article_Collector
>>> collector = Article_Collector(queries)
```

#### Collecting the Articles:
The <i>get_articles()</i> method collects and returns a list of articles. 
It can be passed an optional list of queries to search that will override the list it was instantiated with.
Printing the string representation of the article outputs nicely formatted article information.
```
>>> articles = collector.get_articles()
>>> article = articles[0]
>>> print str(article)

 ----------- Article -----------
Source: Tesla
Title: BlackRock voted to replace Tesla's Musk with independent chairman
Subject: Tesla
Date: 8-31-2018
URL: https://www.reuters.com/article/us-tesla-musk-blackrock/blackrock-voted-to-replace-teslas-musk-with-independent-board-chair-idUSKCN1LG01R
 -------------------------------
```

Article attributes like source, title, date, etc. can be found in the <i>Article.py</i> file's
<i>Article</i> class.

#### Retrieving Article Text:
Parsed article text is retreived on demand for each article with the <i>get_text()</i> method.
```
>>> text = article.get_text()
>>> print text 
... BlackRock-managed funds voted for a measure requiring the chairman be an independent director,
according to BlackRock’s filing with the U.S. Securities and Exchange Commission on Thursday. 
The proposal, which was defeated, would not have affected Musk’s standing as Tesla’s chief 
executive officer. More than 86 million shares voted against the proposal at a shareholder 
meeting in June, while fewer than 17 million voted in favor, Tesla said...
```

#### Finding the Article Subject:
The program can attempt to find the subject of the article with the <i>get_subject()</i> method.
The method takes an optional <i>breadth</i> argument that determines how loose the search is.
Higher values = a looser search.
```
>>> subject = article.get_subject(breadth=5)
>>> print subject
Tesla
```

#### Collecting Information in Bulk:
Text and subjects for a list of articles can be collected with the <i>get_article_info()</i>
method.
Articles without subjects can be filtered with the <i>clean_no_subject()</i> method. This method takes
a list of articles and returns a list of only articles with subjects.
```
>>> collector.get_article_info(articles)
>>> print articles[0].subject
Tesla
>>> print articles[1].subject
Unknown
>>> articles = collector.clean_no_subject(articles)
>>> print articles[1].subject
Tesla 

### Parsing Articles:
Articles in HTML form can be parsed using the <i>parse_HTML()</i> method in the <i>Article_Parser</i> class. 
The method may be run with a document to parse if the parser is not instantiated with a document.

```
>>> import requests
>>> from Article_Parser import Article_Parser
>>> page_html = requests.get("http://fortune.com/2018/08/30/amazons-stock-breaks-above-2000-share-close-trillion-valuation/").text
>>> parser = Article_Parser(page_html)
>>> page_text = parser.parse_HTML()
>>> print page_text
Amazon Market Value Nears $1 Trillion as Shares Cross the $2,000 Milestone
By
Kevin Kelleher
August 30, 2018
Less than a month after Apple became the first U.S. company to be worth at least $1 trillion, Amazon is close to matching that feat.
Amazon shares crossed the $2,000...
```

## Files
- <i>Article_Collector.py</i> - Class for collecting articles
- <i>Article_Parser.py</i> - Parses article content from HTML
- <i>Article.py</i> - Class for holding article information and fetching article text
- <i>requirements.txt</i> - Program requirements
    
