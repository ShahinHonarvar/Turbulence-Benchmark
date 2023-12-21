
from collections import Counter

def if_contains_anagrams(word_list):
    word_counts = Counter("".join(sorted(word.lower())) for word in word_list if len(word) >= 3)
    anagram_count = sum(count*(count-1)//2 for count in word_counts.values())
    return anagram_count >= 66
