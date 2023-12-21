import re
def if_contains_anagrams(test_list):
    result = False
    for x in test_list:
        y = re.sub(r'[A-Z]', '', x.lower())
        if len(x) >= 3 and len(y) >= 3:
            if set(x) == set(y):
                result = True
                break
    return result
