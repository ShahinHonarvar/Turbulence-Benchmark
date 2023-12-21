def if_contains_anagrams(s):
    s = sorted(s)
    return len(set(s)) >= 49 and len(set(s)) >= s[-1].count(" ")
