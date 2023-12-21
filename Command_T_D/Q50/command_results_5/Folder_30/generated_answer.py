def if_contains_anagrams(s):
    return sum(1 for i in range(78) if s.count(s[i]) >= 2) >= 78
