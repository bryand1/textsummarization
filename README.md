# Text Summarization Comparison

### Objective

See and compare the output of popular extractive summarization APIs.

###  Getting started

```bash
git clone https://github.com/bryand1/textsummarization.git
cd textsummarization
pip3 install -r requirements.txt
touch apikeys.env
# Edit apikeys.env with your API keys
# export X_MASHAPE_KEY=[YOUR KEY]
# export SMMRY_KEY=[YOUR KEY]
bash run.sh
```

### APIs Tested

+ [TextAnalysis Text Summarization](https://market.mashape.com/textanalysis/text-summarization)
+ [SMMRY](https://smmry.com/)

#### Text Summarization

```python
# request format
# These code snippets use an open-source library. http://unirest.io/python
response = unirest.post("https://textanalysis-text-summarization.p.mashape.com/text-summarizer-text",
  headers={
    "X-Mashape-Key": "[ENTER KEY HERE]",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  },
  params={
    "sentnum": 5,
    "text": "Automatic summarization is the process of reducing a text document with a computer program in order to create a summary that retains the most important points of the original document. As the problem of information overload has grown, and as the quantity of data has increased, so has interest in automatic summarization. Technologies that can make a coherent summary take into account variables such as length, writing style and syntax. An example of the use of summarization technology is search engines such as Google. Document summarization is another."
  }
)
```

Text Summarization returns a JSON response.

```javascript
{
    "sentences": [
        "Text of sentence #1...",
        "Text of sentence #2...",
        // etc.
    ]
}
```

#### SMMRY

Excerpts from [SMMRY API documentation](https://smmry.com/api)

The API request must be made to https://api.smmry.com. The returned response will be encoded in JSON.

Here are the possible parameters placed in the request URL.
    
+ SM\_API\_KEY=N   Required, your API key.
+ SM\_URL=X   Optional, the webpage to summarize.
+ SM\_LENGTH=N    Optional, the number of sentences returned, default 7.
+ SM\_KEYWORD_COUNT=N     Optional, N the number of keywords to return.
+ SM\_WITH\_BREAK  Optional, inserts the string [BREAK] between sentences.
+ SM\_WITH\_ENCODE     Optional, converts HTML entities to their applicable chars.
+ SM\_IGNORE\_LENGTH   Optional, returns summary regardless of quality or length.
+ SM\_QUOTE\_AVOID     Optional, sentences with quotations will be excluded.
+ SM\_QUESTION\_AVOID  Optional, sentences with question will be excluded.
+ SM\_EXCLAMATION\_AVOID   Optional, sentences with exclamation marks will be excluded.

Here are the possible indexes of the array returned in a JSON array.
    
+ sm\_api\_message     Contains notices, warnings, and error messages.
+ sm\_api\_character_count     Contains the amount of characters returned.
+ sm\_api\_title   Contains the title when available.
+ sm\_api\_content     Contains the summary.
+ sm\_api\_keyword\_array   Contains top ranked keywords in descending order.
+ sm\_api\_error   Contains error code.

```php
$text = "Your long text goes here...";

$ch = curl_init("http://api.smmry.com/&SM_API_KEY=X");
curl_setopt($ch, CURLOPT_HTTPHEADER, array("Expect:")); // See Note
curl_setopt($ch, CURLOPT_POST, true); 
curl_setopt($ch, CURLOPT_POSTFIELDS, "sm_api_input=".$text);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 20);
curl_setopt($ch, CURLOPT_TIMEOUT, 20);
$return = json_decode(curl_exec($ch), true);
curl_close($ch);
```
