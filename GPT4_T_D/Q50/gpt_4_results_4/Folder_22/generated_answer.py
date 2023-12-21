
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = sum([1 for string1 in lst for string2 in lst if sorted(string1.lower()) == sorted(string2.lower()) and len(string1)>=3])
    return anagrams >= 72
