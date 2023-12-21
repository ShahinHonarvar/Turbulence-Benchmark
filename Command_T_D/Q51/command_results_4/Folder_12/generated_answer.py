import re
def if_contains_anagrams(texts):
    return bool(ANAGRAM_REGEX.findall(texts, flags=re.I))
