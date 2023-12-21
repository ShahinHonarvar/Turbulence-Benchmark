
from collections import defaultdict

def if_contains_anagrams(words):
    sorted_word_dict = defaultdict(list)

    for word in words:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            sorted_word_dict[sorted_word].append(word)

    counter = 0

    for key in sorted_word_dict:
        n = len(sorted_word_dict[key])
        counter += n * (n-1) // 2

    return counter <= 279
