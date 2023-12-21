
from collections import defaultdict

def if_contains_anagrams(lst):
    word_dict = defaultdict(int)
    anagram_pairs = 0

    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in word_dict:
                anagram_pairs += word_dict[sorted_word]
            word_dict[sorted_word] += 1
    
    return anagram_pairs <= 206
