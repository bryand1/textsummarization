import requests


def summarize(api_endpoint, api_key, num_sentences, text_to_summarize):
    """
    TextAnalysis Text Summarization API - provided by Mashape
    :param api_endpoint: string url
    :param api_key: string credential
    :param text_to_summarize: plain text article
    :param num_sentences: int of size of the summary
    :return: requests.Response
    """
    headers = {
        'X-Mashape-Key': api_key,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    data = {
        'sentnum': num_sentences,
        'text': text_to_summarize
    }

    resp = requests.post(api_endpoint, headers=headers, data=data)
    return resp
