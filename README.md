# Gpt3TextGeneration

Generate human-like text using OpenAI GPT-3 via a **_text-in, text-out_** API. 

## Overview
GPT-3 is the first-ever generalized language model in the field of natural language processing that can perform equally well on an array of NLP tasks. GPT-3 stands for Generative Pre-trained Transformer that can generate text that is hardly differented from human-generated text.

## Usage

🚧 You need access to the OpenAI API Key to use this Executor: If you dont have the access to the API please apply [here](https://openai.com/api/). 🚧

> Once you have the API KEY, you can pass it as ```uses_with: {'api_key': 'value'}``` along with the Executor name.

#### via Sandbox (recommended)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+sandbox://Gpt3')
```

#### via Docker image

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://Gpt3')
```

#### via source code

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://Gpt3')
```

- To override `__init__` args & kwargs, use `.add(..., uses_with: {'key': 'value'})`
- To override class metas, use `.add(..., uses_metas: {'key': 'value})`

## Examples 

Here is an examples of using the **_GPT3TextGeneration_** Executor:

### Copy Generation

```
Input: "Write a tagline for an ice cream shop:"

Output: The best ice cream in town! 
```