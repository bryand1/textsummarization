# -*- coding: utf-8 -*-
"""
See and compare the output of popular extractive summarization APIs.
@author Bryan Andrade <bryand1@gmail.com>
@version v0.0.1

APIs tested
1. TextAnalysis Text Summarization
2. SMMRY

Usage: python3 main.py [--api textsummarization | smmry]

Args:
--api  Choose which API to test. Default is to run all APIs
"""
import api
import argparse
import config
import os
import util

logger = util.get_logger("main")

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--api', type=str)
    cmdargs = p.parse_args()
    # If cmdargs.api is None, user intends to run all summary APIs
    article = 'uber-vs-lyft.txt'
    with open(os.path.join(config.WD, 'article', article)) as fh:
        text = fh.read()
    logger.info("Loaded article %s", article)
    # TextAnalysis Text Summarization API
    if cmdargs.api == 'textsummarization' or cmdargs.api is None:
        args = (
            config.TEXTSUMMARIZATION_URL,
            config.X_MASHAPE_KEY,
            config.SENTNUM,
            text
        )
        resp = api.textsummarization.summarize(*args)
        js = resp.json()
        output = []
        for i, sentence in enumerate(js['sentences']):
            output.append(f"{i + 1}: {sentence}")
        with open(os.path.join(config.WD, 'output', 'textsummarization.txt'), 'w') as fh:
            fh.write('\n'.join(output))
        logger.info("textsummarization done")

    # SMMRY
    if cmdargs.api == 'smmry' or cmdargs.api is None:
        args = (
            config.SMMRY_URL,
            config.SMMRY_KEY,
            config.SENTNUM,
            text
        )
        resp = api.smmry.summarize(*args)
        js = resp.json()
        with open(os.path.join(config.WD, 'output', 'smmry.txt'), 'w') as fh:
            fh.write(js['sm_api_content'])
        logger.info("smmry done")
