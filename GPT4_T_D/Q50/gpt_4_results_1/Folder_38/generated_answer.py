
from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)

    anagram_pairs = 0
    for group in anagram_dict.values():
        if len(group) > 1:
            anagram_pairs += (len(group)*(len(group)-1))//2
            if anagram_pairs >= 24:
                return True
    return False
