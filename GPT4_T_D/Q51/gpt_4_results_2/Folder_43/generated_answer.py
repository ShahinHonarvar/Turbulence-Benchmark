
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)

    valid_words = [word for word in lst if len(word) >= 3]
    lower_case_words = [word.lower() for word in valid_words]
    anagram_pairs = 0
    word_dict = defaultdict(int)

    for word in lower_case_words:
        word_dict["".join(sorted(word))] += 1

    for value in word_dict.values():
        if value > 1:
            anagram_pairs += ((value-1) * value) // 2

    if anagram_pairs > 3:
        return False
    return True
