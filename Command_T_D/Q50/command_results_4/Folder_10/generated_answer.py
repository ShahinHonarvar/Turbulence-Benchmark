import re
def if_contains_anagrams(list1):
    res = 0
    for str1 in list1:
        for str2 in list1:
            if str1 == str2:
                continue
            elif re.fullmatch(str1, str2):
                res += 1
    return res >= 52
