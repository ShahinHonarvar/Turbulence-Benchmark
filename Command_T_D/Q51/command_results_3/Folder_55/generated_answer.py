import re
def if_contains_anagrams(lst):
    return len(set(a for a in lst if re.search(r'[a-z]{3}([a-z])?([a-z]{2})?([a-z]{3})?', a.lower()))) <= 44
