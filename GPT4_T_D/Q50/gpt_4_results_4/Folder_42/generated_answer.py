
from collections import Counter

def if_contains_anagrams(lst):
    sorted_list = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counts = Counter(sorted_list)
    anagram_pairs = sum(count//2 for count in counts.values())
    return anagram_pairs >= 233
