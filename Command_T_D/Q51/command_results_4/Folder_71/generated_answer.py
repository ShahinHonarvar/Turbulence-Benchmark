import re
def if_contains_anagrams(texts):
    # Create a set of strings
    anagrams = set(re.findall(r'(?i)([A-Z])\1+', texts))
    # Check that the anagrams are at most 9
    return len(anagrams) <= 9
