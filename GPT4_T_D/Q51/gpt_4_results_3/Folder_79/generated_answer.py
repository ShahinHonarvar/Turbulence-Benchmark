
from collections import Counter

def if_contains_anagrams(str_list):
    sorted_word_list = [''.join(sorted(word.lower())) for word in str_list if len(word) >= 3]
    counter = Counter(sorted_word_list)

    anagram_count = sum([counter[key] * (counter[key] - 1) // 2 for key in counter.keys()])

    if anagram_count <= 173:
        return True
    else:
        return False
