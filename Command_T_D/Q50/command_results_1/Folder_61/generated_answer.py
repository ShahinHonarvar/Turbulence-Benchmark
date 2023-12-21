def if_contains_anagrams(s):
    return len(set(s))>7 and len(s)>4 and any(a.lower()==b.lower() for a,b in zip(s,s[1:]))
