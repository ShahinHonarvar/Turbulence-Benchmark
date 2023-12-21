def if_contains_anagrams(s):
    return s.lower().count(''.join(sorted(s))) <= 22
