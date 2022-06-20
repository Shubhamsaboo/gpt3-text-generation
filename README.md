# Gpt3TextGeneration

Generate human-like text using OpenAI GPT-3 via a **_text-in, text-out_** API. 

## Overview
GPT-3 is the first-ever generalized language model in the field of natural language processing that can perform equally well on an array of NLP tasks. It stands for Generative Pre-trained Transformer, which can produce text remarkably similar to that produced by a human.

## Usage

🚧 You need access to the OpenAI API Key to use this Executor: If you don't have access to the API, please apply [here](https://openai.com/api/). 🚧

> Once you have the API KEY, you can pass it as ```uses_with: {'api_key': 'value'}``` along with the Executor name.

To adjust the results according to your use case, you can set the value of `max_token` and `temperature` in the `uses_with` section. To learn more about each of these parameters, check out the [documentation](https://beta.openai.com/docs).

#### via Sandbox (recommended)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+sandbox://Gpt3TextGeneration')
```

#### via Docker image

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://Gpt3TextGeneration')
```

#### via source code

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://Gpt3TextGeneration')
```

- To override `__init__` args & kwargs, use `.add(..., uses_with: {'key': 'value'})`
- To override class metas, use `.add(..., uses_metas: {'key': 'value})`

## Examples 

Here is an example of generating ad copy using the **GPT3TextGeneration** Executor:

```
from jina import Flow
from docarray import Document, DocumentArray

flow = Flow().add(uses='jinahub+sandbox://Gpt3TextGeneration', uses_with=({'api_key': API_KEY}))

text = 'Write a tagline for an ice cream shop:'

with flow:
    da = DocumentArray([Document(text=text) for _ in range(1)])
    r = flow.post(on='/complete', inputs=da)        
    for doc in r:
        print(doc.text)
```
Following is the output produced by the Executor:

```
Output: The best ice cream in town!
```