import re
def if_contains_anagrams(a_list):
    return bool(re.findall(r'(?i)(?=.*\1)', a_list, flags=re.I))
