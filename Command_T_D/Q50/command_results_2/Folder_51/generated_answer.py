def if_contains_anagrams(texts):
    return bool(set(texts) & {a for a in texts for b in texts if a == b})
