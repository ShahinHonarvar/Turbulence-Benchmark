import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?i)(?=([a-z]+\1)+[a-z]+\2)', s)) <= 49
