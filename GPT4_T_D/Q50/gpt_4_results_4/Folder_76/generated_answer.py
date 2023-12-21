
from collections import Counter
def if_contains_anagrams(words):
    word_dict = dict()
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            key = ''.join(sorted(word))
            if key in word_dict:
                word_dict[key].append(word)
            else:
                word_dict[key] = [word]
    anagram_count = sum([len(value)*(len(value)-1)//2 for value in word_dict.values() if len(value) > 1])
    return anagram_count >= 143
