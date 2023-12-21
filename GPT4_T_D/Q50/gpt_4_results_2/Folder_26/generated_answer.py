
from collections import Counter

def if_contains_anagrams(anagrams_list):
    filter_length = [i.lower() for i in anagrams_list if len(i) >= 3]
    anagram_count = Counter([''.join(sorted(word)) for word in filter_length])
    pairs = sum([count//2 for count in anagram_count.values()])
    return True if pairs >= 49 else False
