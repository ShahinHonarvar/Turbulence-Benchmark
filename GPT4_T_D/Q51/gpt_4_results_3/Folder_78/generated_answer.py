
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            c_word = Counter(word)
            for compare_word in lst:
                compare_word = compare_word.lower()
                if word != compare_word and c_word == Counter(compare_word):
                    anagrams.append((word, compare_word))
    return len(anagrams) // 2 <= 70
