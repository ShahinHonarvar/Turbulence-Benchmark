
from collections import defaultdict

def if_contains_anagrams(word_list):
    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    pairs = []
    word_dict = defaultdict(list)

    for word in word_list:
        if len(word) >= 3:
            word_dict[''.join(sorted(word.lower()))].append(word)

    for key in word_dict:
        if len(word_dict[key]) > 1:
            pairs.extend([(word_dict[key][i], word_dict[key][j]) for i in range(len(word_dict[key])) for j in range(i+1, len(word_dict[key]))])

    return len(pairs) >= 277
