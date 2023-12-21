import re
def if_contains_anagrams(test_list):
    res = False
    for t in test_list:
        t = re.sub("(?!^)[a-z]", "", t.lower())
        if t:
            t = t.split()
            for i in range(len(t)):
                for j in range(i + 1, len(t)):
                    if t[i] == t[j]:
                        continue
                    elif t[i] != t[j]:
                        res = True
                        break
    return res
