
from collections import Counter

def if_contains_anagrams(lst):
    sorted_words = []
    anagrams = 0

    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            sorted_words.append(sorted_word)

    count_sorted_words = Counter(sorted_words)

    for count in count_sorted_words.values():
        if count > 1:
            anagrams += count*(count-1)/2

    if anagrams > 70:
        return False
    else:
        return True
