
from collections import defaultdict

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def if_contains_anagrams(lst):
    lst = [i.lower() for i in lst if len(i) >= 3]
    anagrams = defaultdict(list)
    for word in lst:
        anagrams["".join(sorted(word))].append(word)
    
    anagram_pairs = sum(len(value) * (len(value) - 1) // 2 for value in anagrams.values())
    
    if anagram_pairs <= 279:
        return True
    else:
        return False
