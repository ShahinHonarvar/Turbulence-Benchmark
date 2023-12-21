import re
def if_contains_anagrams(lst):
    return bool(re.findall(r'\A[A-Z][A-Z][A-Z][a-z]{%3}\Z' % (len(lst)), lst))
