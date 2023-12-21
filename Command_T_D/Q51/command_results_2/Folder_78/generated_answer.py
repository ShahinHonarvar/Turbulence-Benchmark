def if_contains_anagrams(s):
    return s.count("".join(sorted(str(a).lower()))) <= 70
