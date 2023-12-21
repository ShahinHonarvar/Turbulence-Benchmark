import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?i)(?<=.)(.*?)(?=.)', s)) >= 194
