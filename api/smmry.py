import requests


def summarize(api_endpoint, api_key, num_sentences, text_to_summarize):
    """
    SMMRY - text summarization API
    :param api_endpoint: string url
    :param api_key: string credential
    :param text_to_summarize: plain text article
    :param num_sentences: int of size of the summary
    :return: requests.Response
    """
    url = "{}/?SM_API_KEY={}&SM_LENGTH={}".format(
        api_endpoint, api_key, num_sentences)
    data = {'sm_api_input': text_to_summarize}
    resp = requests.post(url, data=data)
    return resp
