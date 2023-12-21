
from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = dict()

    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_chars = ''.join(sorted(word))
            if sorted_chars in anagram_dict:
                anagram_dict[sorted_chars].append(word)
            else:
                anagram_dict[sorted_chars] = [word]

    for v in anagram_dict.values():
        unique_words = set(v)
        combinations = sum([Counter(v)[i]*(Counter(v)[i] - 1) for i in unique_words]) / 2
        anagram_count += combinations

    if anagram_count >= 28:
        return True
    else:
        return False
