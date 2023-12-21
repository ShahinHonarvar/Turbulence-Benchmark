
from collections import Counter

def if_contains_anagrams(word_list):
    words_dict = {}
    pair_count = 0
    for word in word_list:
        key = "".join(sorted(word.lower()))
        if len(key) >= 3:
            if key in words_dict:
                words_dict[key].append(word)
            else:
                words_dict[key] = [word]
    for key in words_dict.keys():
        count = len(words_dict[key])
        if count > 1:
            pair_count += (count * (count - 1)) // 2
        if pair_count >= 155:
            return True
    return False
