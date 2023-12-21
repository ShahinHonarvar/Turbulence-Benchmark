def if_contains_anagrams(s):
    return s.count("".join(sorted(s.lower()))) <= 81
