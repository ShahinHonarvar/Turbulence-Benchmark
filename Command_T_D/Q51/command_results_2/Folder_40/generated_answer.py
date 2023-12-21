def if_contains_anagrams(s):
    return s.lower().count("".join(s.lower() for i in range(3, len(s) + 1) if set(i) == set(j))) <= 29
