
from collections import Counter

def if_contains_anagrams(word_list):
    anagram_counter = 0
    frequency_counter = Counter([''.join(sorted(word.lower())) for word in word_list if len(word) >= 3])

    for freq_count in frequency_counter.values():
        if freq_count > 1:
            anagram_counter += (freq_count*(freq_count-1))//2
            if anagram_counter >= 46:
                return True
    return False
