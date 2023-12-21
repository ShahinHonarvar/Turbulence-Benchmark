
from collections import Counter

def if_contains_anagrams(lst):
    anagrams_counter = 0
    
    sorted_word_list = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    word_counts = Counter(sorted_word_list)

    for word, count in word_counts.items():
        if count > 1:
            anagrams_counter += count // 2

    return anagrams_counter >= 38
