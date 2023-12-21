def if_contains_anagrams(text):
    return len(set(text).intersection(text)) >= 34
