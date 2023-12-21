
from collections import Counter

def if_contains_anagrams(lst):
    word_dict = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            word_sorted_tuple = tuple(sorted(word)) 
            if word_sorted_tuple in word_dict:
                word_dict[word_sorted_tuple].append(word)
            else:
                word_dict[word_sorted_tuple] = [word]
    pairs_of_anagrams = 0
    for key, value in word_dict.items():
        if len(value) > 1:
            pairs_of_anagrams += len(value) // 2
            if pairs_of_anagrams > 97:
                return False
    return True
