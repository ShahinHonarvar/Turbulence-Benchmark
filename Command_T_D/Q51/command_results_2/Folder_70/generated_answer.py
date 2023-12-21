def if_contains_anagrams(text):
    return len(text) > 2 and len(text) <= 97 and len(set(text)) <= 98 and len(set(text)) == len(text) and len(set(text)) == len(set(lower(text)))
