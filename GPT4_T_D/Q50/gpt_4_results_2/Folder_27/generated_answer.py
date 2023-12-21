
from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    word_dict = defaultdict(list)

    for word in list_of_strings:
        key = "".join(sorted(word.lower()))
        if len(key) >= 3:
            word_dict[key].append(word)
    
    pairs_counter = 0
    for key, words in word_dict.items():
        pairs_counter += len(words)*(len(words)-1) // 2
    
    return pairs_counter >= 86
