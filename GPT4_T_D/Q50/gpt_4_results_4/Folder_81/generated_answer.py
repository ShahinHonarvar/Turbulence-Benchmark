
from collections import Counter

def if_contains_anagrams(words):
    word_dict = {}
    for word in words:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key in word_dict:
                word_dict[key].append(word)
            else:
                word_dict[key] = [word]

    pairs = sum([len(value)*(len(value)-1)//2 for value in word_dict.values() if len(value) > 1])

    return pairs >= 16
