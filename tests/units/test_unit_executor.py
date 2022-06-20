from executor import Gpt3
import os
from docarray import DocumentArray, Document

_API_KEY = os.environ.get('API_KEY')

_max_tokens= 20
_temperature = 0.7

def test_complete():

    executor = Gpt3(api_key=_API_KEY)

    text = 'Write a tagline for an ice cream shop:'

    da = DocumentArray([Document(text=text) for _ in range(1)])
    executor.completion(da) 

    for doc in da:
        assert len(doc.text) > 0


def test_complete_wo_api_key():

    executor = Gpt3()

    text = 'Write a tagline for an ice cream shop:'

    da = DocumentArray(
        [Document(text=text, tags={'api_key': _API_KEY}) for _ in range(1)]
    )
    executor.completion(da)

    for doc in da:
        assert len(doc.text) > 0

def test_complete_wo_max_tokens():

    executor = Gpt3()

    text = 'Write a tagline for an ice cream shop:'

    da = DocumentArray(
        [Document(text=text, tags={'api_key': _API_KEY, 'max_tokens': _max_tokens}) for _ in range(1)]
    )
    executor.completion(da)

    for doc in da:
        assert len(doc.text) > 0

def test_complete_wo_temperature():

    executor = Gpt3()

    text = 'Write a tagline for an ice cream shop:'

    da = DocumentArray(
        [Document(text=text, tags={'api_key': _API_KEY, 'temperature': _temperature}) for _ in range(1)]
    )
    executor.completion(da)

    for doc in da:
        assert len(doc.text) > 0