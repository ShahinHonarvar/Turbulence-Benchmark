
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            for other_word in lst:
                other_word = other_word.lower()
                if word != other_word and Counter(word) == Counter(other_word):
                    anagrams.append((word, other_word))
    return len(anagrams) / 2 <= 15
