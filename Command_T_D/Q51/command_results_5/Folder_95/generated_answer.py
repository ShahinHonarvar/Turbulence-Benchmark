import re
def if_contains_anagrams(text):
    anagrams = re.findall(r'\A[a-z]+[a-z]+[a-z]+', text.lower())
    return len(anagrams) <= 6
