
from collections import Counter

def if_contains_anagrams(str_list):
    word_dict = {}
    for word in str_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = "".join(sorted(word))
            if sorted_word in word_dict:
                word_dict[sorted_word] += 1
            else:
                word_dict[sorted_word] = 1

    pair_count = sum([count * (count-1) // 2 for count in word_dict.values()])

    return pair_count >= 91
