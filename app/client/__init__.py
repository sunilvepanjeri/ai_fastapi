import settings
import os
import openai
import asyncio
from functools import lru_cache


async def module_values():
    attributes, functions, classes = [], [], []
    for item in dir(openai):
        attr = getattr(openai, item)
        if callable(attr):
            if isinstance(attr, type):
                classes.append(attr)
            else:
                functions.append(attr)
        else:
            attributes.append(item)
    return attributes, functions, classes

@lru_cache()
async def openai_models():
    models = []
    for model in openai.models.list().data:
        models.append(model.id)
    return models

if __name__ == "__main__":
    data = asyncio.run(openai_models())
    print(data)