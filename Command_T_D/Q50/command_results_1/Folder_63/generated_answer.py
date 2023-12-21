import collections
def if_contains_anagrams(s):
    return sum(s.count(s[j]) > 1 for j in range(len(s))) >= 89
