import collections
def if_contains_anagrams(s):
    res = False
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            x = collections.Counter(s[i].lower())
            y = collections.Counter(s[j].lower())
            if x == y:
                res = True
                break
            elif x != y:
                res = True
                break
    return res
