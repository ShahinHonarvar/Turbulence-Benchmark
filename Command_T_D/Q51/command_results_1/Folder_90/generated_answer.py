def if_contains_anagrams(s):
    return sum(a == b for a, b in zip(s, set(s))) <= 147
