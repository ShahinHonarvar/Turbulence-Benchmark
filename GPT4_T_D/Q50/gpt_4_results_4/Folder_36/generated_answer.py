
from collections import Counter
from itertools import combinations

def if_contains_anagrams(word_list):
    valid_words = [word.lower() for word in word_list if len(word) >= 3]
    
    sorted_words = [''.join(sorted(word)) for word in valid_words]
    
    word_counts = Counter(sorted_words)

    anagram_pairs = sum(count*(count-1)//2 for count in word_counts.values())

    return anagram_pairs >= 312
