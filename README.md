# Google News Article Collector
### Author: Peter Swanson
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 2.7](https://img.shields.io/badge/Python-2.7-brightgreen.svg)](https://www.python.org/downloads/release/python-2714/)
[![requests 2.19.1](https://img.shields.io/badge/requests-2.19.1-brightgreen.svg)](https://pypi.org/project/requests/)

## Background
Online news articles are incredibly valuable to data scientists seeking to understand long-term trends.
One of the most difficult parts of analyzing these articles is parsing them. 
Online news articles collected via script must be parsed from the HTML of the page they are hosted on. 

<b>This application makes collecting and parsing stories from Google News incredibly easy!</b>

This repository contains the Python code for collecting and parsing articles, as well as a sample driver.

## Running the Application
### Installing dependencies:
Ensure the following are installed on the machine you are running the application on:
- Python 2.7 with Pip
- Virtualenv for Python 2.7

Create a virtualenv and install the requirements from <i>requirements.txt</i> with Pip
```
$ pip install -r "requirements.txt"
``` 

### Running the driver:
The driver can be run with Python:
```
$ python driver.py
```

By default, the driver collects articles based on the queries "Fortune" and "Seeking Alpha", then
prints the parsed text of the first article.

### Using the article collector:
The article collector can be used from Python code or the console if imported.
It can be instantiated with a list of queries or given a list of queries later on.

#### Instantiation:
```
>>> queries = ["Tesla"]
>>> from Article_Collector import Article_Collector
>>> collector = Article_Collector(queries)
```

#### Collecting Articles:
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

## Files
- <i>Article_Collector.py</i> - Class for collecting articles
- <i>Article.py</i> - Class for holding article information and fetching article text
    
