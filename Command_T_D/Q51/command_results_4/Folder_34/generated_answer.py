import re
def if_contains_anagrams(lst):
    return bool(re.findall(r'(?i)(?<=.)(.*?)(?=.)', *lst))
