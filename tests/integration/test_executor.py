from executor import Gpt3TextGeneration
import os
from docarray import DocumentArray, Document 
from jina import Flow

_API_KEY = os.environ.get('API_KEY')
_max_tokens= 20
_temperature = 0.7

def test_complete():

    flow = Flow().add(uses=Gpt3TextGeneration, uses_with=({'api_key': _API_KEY}))

    text = 'Write a tagline for an ice cream shop:'

    with flow:
        da = DocumentArray([Document(text=text) for _ in range(1)])

        response_da = flow.post(on='/complete', inputs=da)

        for doc in response_da:
            assert len(doc.text) > 0

def test_complete_wo_api_key():

    text = 'Write a tagline for an ice cream shop:'

    flow = Flow().add(uses=Gpt3TextGeneration, uses_with={'api_key': _API_KEY})

    with flow:

        da = DocumentArray(
            [Document(text=text) for _ in range(1)]
        )
        response_da = flow.post(on='/complete', inputs=da)

        for doc in response_da:
            assert len(doc.text) > 0

def test_complete_wo_max_tokens():

    text = 'Write a tagline for an ice cream shop:'

    flow = Flow().add(uses=Gpt3TextGeneration, uses_with={'api_key': _API_KEY, 'max_tokens': _max_tokens})

    with flow:

        da = DocumentArray(
            [Document(text=text) for _ in range(1)]
        )
        response_da = flow.post(on='/complete', inputs=da)

        for doc in response_da:
            assert len(doc.text) > 0

def test_complete_wo_temperature():

    text = 'Write a tagline for an ice cream shop:'

    flow = Flow().add(uses=Gpt3TextGeneration, uses_with={'api_key': _API_KEY, 'temperature': _temperature})

    with flow:

        da = DocumentArray(
            [Document(text=text) for _ in range(1)]
        )
        response_da = flow.post(on='/complete', inputs=da)

        for doc in response_da:
            assert len(doc.text) > 0
