
from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    anagram_count = 0
    for word in lst:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if word not in anagram_dict:
                anagram_dict[word] = 1
            else:
                anagram_count += anagram_dict[word]
                anagram_dict[word] += 1
    return anagram_count <= 58
