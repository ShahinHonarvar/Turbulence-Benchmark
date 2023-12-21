import re
def if_contains_anagrams(str_list):
    return bool(re.findall(r'(?=([A-Z]+[a-z]+[A-Z]))([A-Z]+[a-z]+[A-Z])', ' '.join(map(str.lower, str_list)), flags=re.I))
