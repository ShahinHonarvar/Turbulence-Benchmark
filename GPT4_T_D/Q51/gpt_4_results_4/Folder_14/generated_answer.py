
from collections import defaultdict

def anagram_pairs(words):
    groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            groups[str(sorted(word.lower()))].append(word)
    return sum(len(group)*(len(group)-1)//2 for group in groups.values() if len(group) > 1)

def if_contains_anagrams(lst): 
    return anagram_pairs(lst) <= 474
