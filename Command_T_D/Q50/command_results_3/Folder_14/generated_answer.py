import collections
def if_contains_anagrams(s):
    return bool(len(s)>=22 and len(s[::2])>=11 and len(s[1::2])>=11 and all(a==b for a,b in zip(s[::2],s[1::2]) and a.lower()==b.lower()))
