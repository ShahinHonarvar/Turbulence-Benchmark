
from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    pairs = sum([(Counter(lst) - Counter(set(lst)))[i] for i in anagram_dict.values() if len(i) >= 2])
    if pairs >= 144:
        return True
    return False
