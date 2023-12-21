import re
def if_contains_anagrams(input_list):
    res = True
    for s in input_list:
        if len(s) >= 3:
            res &= any(a == b for a, b in zip(re.findall(r'((?i)(?<=.)\1)', s), input_list))
    return res
