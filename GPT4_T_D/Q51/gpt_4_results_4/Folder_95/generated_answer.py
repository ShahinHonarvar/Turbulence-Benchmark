
from collections import Counter


def if_contains_anagrams(list_of_strings):
    anagrams = []
    for word in list_of_strings:
        word = word.lower()
        if len(word) >= 3:
            for other_word in list_of_strings:
                other_word = other_word.lower()
                if word != other_word:
                    if Counter(word) == Counter(other_word):
                        anagrams.append((word, other_word))
    return len(set(tuple(sorted(t)) for t in anagrams)) <= 6
