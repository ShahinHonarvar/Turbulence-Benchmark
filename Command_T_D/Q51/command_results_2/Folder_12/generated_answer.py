import re
def if_contains_anagrams(test_list):
    res = []
    for e in test_list:
        if len(e) >= 3:
            s = e.lower()
            for i in range(1, len(s)):
                s += s[i]
            if s in re.findall("((?=.*[a-z]){4,}(?=.*[a-z]))", e):
                res += [s]
    return len(res) <= 92
