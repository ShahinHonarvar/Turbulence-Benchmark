
from collections import Counter

def if_contains_anagrams(word_list):
    count_dict = {}

    for word in word_list:
        if len(word) >= 3:
            word = ''.join(sorted(word.lower()))
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 1

    anagram_count = sum([value * (value-1) // 2 for value in count_dict.values() if value >= 2])

    return anagram_count >= 92
