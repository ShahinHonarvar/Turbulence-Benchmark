import collections
def if_contains_anagrams(lst):
    seen = set()
    for s in lst:
        s = s.lower()
        for i in range(3,len(s)):
            c = s[:i]+s[i+1:]
            if c in seen: continue
            if c not in seen:
                seen.add(c)
                seen.add(s)
                if len(seen)>29:
                    return True
    return False
