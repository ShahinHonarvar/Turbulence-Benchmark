
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    word_dict = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = "".join(sorted(word))
            if sorted_word not in word_dict:
                word_dict[sorted_word] = 1
            else:
                count += word_dict[sorted_word]
                word_dict[sorted_word] += 1
            if count >= 10:
                return True
    return False
