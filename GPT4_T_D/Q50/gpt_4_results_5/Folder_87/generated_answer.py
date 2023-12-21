
from collections import Counter

def if_contains_anagrams(lst):
    cnt = 0
    anagram_dict = {}

    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = 1
            else:
                cnt += anagram_dict[sorted_word]
                anagram_dict[sorted_word] += 1

    if cnt >= 88:
        return True
    else:
        return False
