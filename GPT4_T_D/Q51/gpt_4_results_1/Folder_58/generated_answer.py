
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)

    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams["".join(sorted(word.lower()))].append(word)
    
    pairs = sum([len(vals)*(len(vals)-1)//2 for vals in anagrams.values()])
    return pairs <= 60
