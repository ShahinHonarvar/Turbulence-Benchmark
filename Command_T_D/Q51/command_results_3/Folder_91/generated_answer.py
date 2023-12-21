import re
def if_contains_anagrams(list_str):
    res = False
    for str1 in list_str:
        for str2 in list_str:
            if(str1.lower() == str2.lower()):
                res = True
    return res
