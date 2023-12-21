
from collections import Counter

def if_contains_anagrams(lst):
    anagrams_dict = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams_dict:
                anagrams_dict[sorted_word].append(word)
            else:
                anagrams_dict[sorted_word] = [word]

    pairs = 0
    for words_list in anagrams_dict.values():
        counter = Counter(words_list)
        for count in counter.values():
            pairs += count // 2

    return pairs >= 209
