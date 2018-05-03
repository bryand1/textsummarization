import os
import logging

WD = os.path.dirname(os.path.abspath(__file__))

LOGLEVEL = logging.INFO
LOGFMT = "%(asctime)s %(name)s %(levelname)s %(message)s"
DATEFMT = "%Y-%m-%d %H:%M:%S"

X_MASHAPE_KEY = os.environ.get('X_MASHAPE_KEY')

TEXTSUMMARIZATION_URL = 'https://textanalysis-text-summarization.p.mashape.com/text-summarizer-text'
SMMRY_URL = 'https://api.smmry.com'
SMMRY_KEY = os.environ.get('SMMRY_KEY')
# Number of sentences in summary output
SENTNUM = 10
