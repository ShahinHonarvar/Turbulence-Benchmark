
from collections import Counter

def if_contains_anagrams(words_list):
    counter = Counter()
    for word in words_list:
        word = word.lower()
        if len(word) > 2:
            counter[''.join(sorted(word))] += 1

    anagram_pairs = 0
    for count in counter.values():
        anagram_pairs += (count - 1)

    return anagram_pairs <= 40
