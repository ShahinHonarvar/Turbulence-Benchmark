import re
def if_contains_anagrams(test_list):
    res = True
    for x in test_list:
        if len(x) >= 3:
            s = str(x)
            for i in range(len(s)):
                s = s[:i] + s[i+1:]
                if s in test_list:
                    res = False
                    break
            if res == False:
                break
    return res
