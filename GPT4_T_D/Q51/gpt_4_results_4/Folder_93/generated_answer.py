
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            for another_word in lst:
                another_word = another_word.lower()
                if word != another_word and sorted(word) == sorted(another_word):
                    if sorted([word, another_word]) not in anagrams:
                        anagrams.append(sorted([word, another_word]))
    return len(anagrams) <= 36
