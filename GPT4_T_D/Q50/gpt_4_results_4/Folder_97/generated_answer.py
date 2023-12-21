
from collections import defaultdict

def if_contains_anagrams(lst):
    dict_anagram = defaultdict(list)
    count = 0

    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = "".join(sorted(word_lower))
            dict_anagram[sorted_word].append(word_lower)

    for key in dict_anagram:
        l = len(dict_anagram[key])
        count += l * (l - 1) // 2

    return count >= 123
