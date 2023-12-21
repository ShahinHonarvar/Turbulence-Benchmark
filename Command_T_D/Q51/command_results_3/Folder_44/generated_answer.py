import re
def if_contains_anagrams(test_list):
    res = len(test_list) >= 3
    for item in test_list:
        res &= re.sub(r'[A-z]', '', item.lower()) not in test_list
    return res <= 75
