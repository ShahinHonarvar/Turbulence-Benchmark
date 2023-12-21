def if_contains_anagrams(s):
    return s.count("".join(sorted(str(i), key=str.lower))) > 15
