
def if_contains_anagrams(words):
    from collections import defaultdict
    from itertools import combinations

    anagrams_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagrams_dict[sorted_word].append(word)
    
    anagram_pairs = [list(combinations(values, 2)) for values in anagrams_dict.values() if len(values) > 1]
    flattened_pairs = [pair for sublist in anagram_pairs for pair in sublist]

    return len(flattened_pairs) >= 24
