def if_contains_anagrams(texts):
    return len(set(texts).intersection(*(set(x) for x in texts))) > 2
