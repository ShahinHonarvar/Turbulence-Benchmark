import re
def if_contains_anagrams(text):
    return len(set(re.findall(r'(?i)(?<=.)(.*?)(?=.)')))>=115
