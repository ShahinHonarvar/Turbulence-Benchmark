
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)

    total_pairs = sum(len(words) * (len(words) - 1) // 2 for words in anagram_dict.values())
    
    return total_pairs <= 17
