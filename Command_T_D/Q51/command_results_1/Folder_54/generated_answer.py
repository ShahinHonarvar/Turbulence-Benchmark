import re
def if_contains_anagrams(s):
    return len(re.findall(r'\A[A-Za-z]{3}(?=\w[A-Za-z]{2})', ''.join(s), flags=re.I)) <= 39
