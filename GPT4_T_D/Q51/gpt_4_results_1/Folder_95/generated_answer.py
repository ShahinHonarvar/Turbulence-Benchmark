
from collections import Counter

def if_contains_anagrams(words_list):
    anagrams = []
    words_list = [word.lower() for word in words_list if len(word) >= 3]
    for word in words_list:
        word_counter = Counter(word)
        for possible_anagram in words_list[words_list.index(word)+1:]:
            if word_counter == Counter(possible_anagram):
                anagrams.append((word, possible_anagram))
    return len(anagrams) <= 6
