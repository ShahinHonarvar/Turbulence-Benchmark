def if_contains_anagrams(lst):
    res = False
    for s in lst:
        lst.remove(s)
        for m in range(3, len(s)):
            if s[m] != ' ':
                tmp = s[:m] + s[m + 1:]
                if len(tmp) == len(s) and sorted(tmp.lower()) == sorted(s.lower()):
                    res = True
                    break
            else:
                break
    return res
