import re
def if_contains_anagrams(test_list):
    return bool(re.findall(r'(?i)(?=.*[A-Z])([a-z]+)(?=.*[A-Z])([a-z]+)', test_list))
