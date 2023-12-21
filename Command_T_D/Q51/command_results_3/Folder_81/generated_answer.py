import re
def if_contains_anagrams(s):
    return len(set(re.findall(r'(?i)(?:[a-z]){3}){2}', s))) <= 79
