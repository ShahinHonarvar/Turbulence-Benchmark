
from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    anagram_pairs = sum([Counter(words).most_common(1)[0][1] - 1 for words in anagram_dict.values() if len(words) > 1])
    return anagram_pairs <= 40
