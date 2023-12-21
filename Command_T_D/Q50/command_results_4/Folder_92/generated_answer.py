import re
def if_contains_anagrams(test_list):
    res = False
    for x in test_list:
        if len(x) >= 3:
            y = str(x).lower()
            res |= re.findall(r'(?i)(?=.*?%s)' % y, y)
            if len(res) >= 2:
                break
    return res
