
from collections import defaultdict

def if_contains_anagrams(word_list):
    anagrams_dict = defaultdict(list)
    for word in word_list:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams_dict[sorted_word].append(word)

    pairs_count = 0
    for word, anagrams in anagrams_dict.items():
        pairs_count += len(anagrams) * (len(anagrams) - 1) / 2

    if pairs_count >= 233:
        return True
    else:
        return False
