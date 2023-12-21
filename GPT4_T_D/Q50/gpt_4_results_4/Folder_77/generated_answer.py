
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagram_dict = defaultdict(list)
    
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)

    pairs_count = sum(len(words) * (len(words) - 1) // 2 for words in anagram_dict.values())
    
    return pairs_count >= 209
