def if_contains_anagrams(s):
    return s.count("".join(sorted(a))) >= 16 for a in zip(*[iter(s)]*3) if len(a) >= 3
