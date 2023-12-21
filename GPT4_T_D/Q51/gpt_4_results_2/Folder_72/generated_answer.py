
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    words_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            words_dict[sorted_word].append(word)

    counter = 0
    for anagrams in words_dict.values():
        if len(anagrams) > 1:
            counter += len(anagrams) * (len(anagrams) - 1) // 2

    return counter <= 188
