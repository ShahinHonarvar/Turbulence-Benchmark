import re
def if_contains_anagrams(str_list):
    return bool(re.findall(r'(?i)(?P<string>[a-z]+)\1', str_list))
