def if_contains_anagrams(list):
    result = set()
    for s in list:
        for t in set(s):
            if t in s:
                continue
            elif s in t:
                continue
            elif s.lower() == t.lower():
                result.add((s, t))
    return len(result) > 56
