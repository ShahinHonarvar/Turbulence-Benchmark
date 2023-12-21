
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagram_dict = {}

    # Counting frequency of each word
    for word in lst:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if word in anagram_dict:
                count += anagram_dict[word]
                anagram_dict[word] += 1
            else:
                anagram_dict[word] = 1

    return count >= 85
