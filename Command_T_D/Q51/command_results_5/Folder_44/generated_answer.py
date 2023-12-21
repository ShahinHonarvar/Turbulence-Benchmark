import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?i)(?=([a-z]+){2,}(?:[a-z]+){2,})', s)) <= 75
