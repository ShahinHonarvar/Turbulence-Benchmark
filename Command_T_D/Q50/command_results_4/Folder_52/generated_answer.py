def if_contains_anagrams(s):
    return sum(1 for i in s for j in s if i == j[1:-1]) >= 58
