
from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_pairs = defaultdict(set)
    for idx, word in enumerate(string_list):
        sorted_word = ''.join(sorted(word.lower()))
        for anagram in string_list[idx+1:]:
            if len(anagram) < 3:
                continue
            if ''.join(sorted(anagram.lower())) == sorted_word:
                anagram_pairs[word].add(anagram)

    pair_count = sum(len(values) for key, values in anagram_pairs.items())

    if pair_count <= 20:
        return True
    else:
        return False
