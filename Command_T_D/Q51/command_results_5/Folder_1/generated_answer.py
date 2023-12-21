import re
def if_contains_anagrams(test_list):
    res = False
    for e in test_list:
        s = str(e)
        for c in s:
            if c.lower() not in 'qwertyuiopasdfghjklzxcvbnm': continue
            s = s.replace(c, '').lower()
            if re.search(s, s[1:]): res = True
            break
    return res
