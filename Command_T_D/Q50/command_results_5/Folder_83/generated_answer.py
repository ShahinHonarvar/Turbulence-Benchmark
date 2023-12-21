import re
def if_contains_anagrams(texts):
    anagrams = [(text, re.sub(r'[A-Z]', '', text)) for text in texts if len(text) >= 3]
    return len(set(anagrams)) >= 48
