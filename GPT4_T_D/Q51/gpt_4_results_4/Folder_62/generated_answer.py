
from collections import defaultdict

def if_contains_anagrams(words_list):
    anagrams = defaultdict(list)
    for word in words_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)

    pairs_count = sum(len(words)*(len(words)-1)//2 for words in anagrams.values())

    return pairs_count <= 289
