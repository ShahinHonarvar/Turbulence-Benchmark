
from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams_dict = defaultdict(list)

    for word in str_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams_dict[sorted_word].append(word)

    count = 0
    for sorted_word, anagrams in anagrams_dict.items():
        n = len(anagrams)
        count += n * (n - 1) // 2

    if count <= 78:
        return True
    else:
        return False
