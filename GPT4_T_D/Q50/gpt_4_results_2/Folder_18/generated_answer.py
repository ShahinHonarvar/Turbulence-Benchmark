
from collections import defaultdict

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def if_contains_anagrams(lst):
    word_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            word_dict[sorted_word].append(word)

    count = 0
    for word_list in word_dict.values():
        count += len(word_list) * (len(word_list) - 1) // 2

    return count >= 106
