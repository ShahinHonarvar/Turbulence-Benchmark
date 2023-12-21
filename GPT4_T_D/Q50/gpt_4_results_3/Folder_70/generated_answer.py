
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    anagrams = 0
    for i in range(len(lst)):
        if len(lst[i]) < 3:
            continue
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagrams += 1
    return anagrams >= 189
