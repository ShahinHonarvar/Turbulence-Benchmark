
from collections import defaultdict

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def if_contains_anagrams(lst):
    checked = defaultdict(int)
    for string in lst:
        checked[''.join(sorted(string.lower()))] += 1

    pairs = sum((v * (v-1))//2 for v in checked.values())

    return pairs <= 39
