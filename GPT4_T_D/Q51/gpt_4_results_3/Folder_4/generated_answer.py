
from collections import defaultdict

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def if_contains_anagrams(list_of_strings):
    anagram_pairs = defaultdict(list)
    for s in list_of_strings:
        if len(s) >= 3:
            anagram_pairs[''.join(sorted(s.lower()))].append(s)
    count = sum(len(v)*(len(v)-1)//2 for v in anagram_pairs.values())
    return count <= 84
