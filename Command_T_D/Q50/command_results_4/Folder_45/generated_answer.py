def if_contains_anagrams(s):
    s=sorted(set(s),key=lambda x: x.lower())
    return len(s)>274 and len(s[-1])>2
