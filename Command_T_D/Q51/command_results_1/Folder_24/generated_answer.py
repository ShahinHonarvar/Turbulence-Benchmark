def if_contains_anagrams(s):
    return len(s) <= 96 and all(str(i).lower() == str(j).lower() for i, j in zip(s, s))
