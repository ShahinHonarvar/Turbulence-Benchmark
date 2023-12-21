
from collections import Counter

def if_contains_anagrams(lst):
    word_dict = {}
    counter = 0

    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = "".join(sorted(word))
            if sorted_word in word_dict:
                counter += 1
                if counter >= 115:
                    return True
            else:
                word_dict[sorted_word] = 1
    return False
