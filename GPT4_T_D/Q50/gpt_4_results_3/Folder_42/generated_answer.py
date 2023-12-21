
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    sorted_word_lst = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    word_frequency = Counter(sorted_word_lst)
    for frequency in word_frequency.values():
        count += frequency * (frequency - 1) // 2
    return count >= 233
