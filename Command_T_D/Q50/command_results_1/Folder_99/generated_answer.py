import re
def if_contains_anagrams(list_str):
    return bool(re.findall(r'(?i)(?<=.)(.*?)(?<=.)\1', *list_str))
