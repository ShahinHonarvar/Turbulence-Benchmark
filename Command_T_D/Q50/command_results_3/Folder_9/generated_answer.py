import re
def if_contains_anagrams(test_list):
    return bool(re.findall(r'(?i)(?P<string>.{3,})(?P< reversal>.{3,})', test_list))
