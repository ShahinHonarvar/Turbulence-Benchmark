import re
def if_contains_anagrams(s):
    return not re.findall(r'(?i)(?<=.)(.*?)(?=.)\1', ' '.join(s))
