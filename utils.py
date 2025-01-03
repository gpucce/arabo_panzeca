import json
from itertools import islice

def get_keywords(text=None):
    # some code here
    if text is None:
        text = "keywords.jsonl"
    with open(text, "r") as f:
        keywords = [json.loads(i) for i in f.readlines()]
    return keywords

def contains_arabic(text):
    try:
        # Arabic Unicode ranges
        arabic_ranges = [
            (0x0600, 0x06FF),  # Arabic
            (0x0750, 0x077F),  # Arabic Supplement
            (0x08A0, 0x08FF)   # Arabic Extended-A
        ]

        # Check if any character in the text is within the Arabic ranges
        for char in text:
            if any(start <= ord(char) <= end for start, end in arabic_ranges):
                return True
    except:
        return False
    return False

def batched(iterable, n):
    # batched('ABCDEFG', 3) → ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        yield batch

