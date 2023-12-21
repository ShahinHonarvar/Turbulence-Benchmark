
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        c1 = Counter(s1.lower())
        c2 = Counter(s2.lower())
        return c1 == c2

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) > 2 and len(lst[j]) > 2 and is_anagram(lst[i], lst[j]):
                count += 1
    return count <= 40
