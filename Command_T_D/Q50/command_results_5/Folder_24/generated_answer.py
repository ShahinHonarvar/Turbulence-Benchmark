import collections
def if_contains_anagrams(s):
    lst = []
    for i in range(len(s)):
        x = s[i]
        for j in range(len(x)):
            for k in range(j+1, len(x)):
                s[i] = x[:j] + x[k:] + x[j+1:]
                if s[i] in lst:
                    lst.remove(s[i])
                    break
    return len(lst) >= 65
