
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)

    count = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2

    return count <= 74
