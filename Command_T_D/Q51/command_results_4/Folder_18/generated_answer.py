import re
def if_contains_anagrams(lst):
    return len(re.findall(r'(?i)(?:[a-z]+){2,}(?:[a-z]+){2,}', ' '.join(lst))) <= 42
