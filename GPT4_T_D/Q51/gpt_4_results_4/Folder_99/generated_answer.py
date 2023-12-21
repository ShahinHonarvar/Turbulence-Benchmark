
from collections import Counter

def if_contains_anagrams(word_list):
    anagrams = []
    for word in word_list:
        if len(word) < 3:
            continue
        word_counter = Counter(word.lower())
        for other_word in word_list:
            if word != other_word and word_counter == Counter(other_word.lower()):
                if (word, other_word) not in anagrams and (other_word, word) not in anagrams:
                    anagrams.append((word, other_word))
    if len(anagrams) <= 93:
        return True
    else:
        return False
