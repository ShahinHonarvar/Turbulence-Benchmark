
from collections import Counter

def if_contains_anagrams(word_list):
    word_dict = {}
    for word in word_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in word_dict:
                word_dict[sorted_word] += 1
            else:
                word_dict[sorted_word] = 1

    anagram_pairs = sum([count * (count-1) // 2 for count in word_dict.values()])
    if anagram_pairs >= 49:
        return True
    else:
        return False
