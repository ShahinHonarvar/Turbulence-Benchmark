def if_contains_anagrams(list):
    return sum(sum(0 if a == b else 1 for a, b in zip(s, s.swapcase())) >= 7 for s in list) >= 7
