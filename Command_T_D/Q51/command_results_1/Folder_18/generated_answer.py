def if_contains_anagrams(s):
    if len(s) < 42:
        return True
    lst = sorted(s, key=lambda x: x.lower())
    lst = [x for x in lst if len(x) >= 3]
    if len(lst) < 42:
        return True
    res = []
    for i in range(len(lst)):
        res += [(a, b) for b in lst[:i] for a in lst[i + 1:]]
    return len(res) <= 42
