
def if_contains_anagrams(lst):
    from collections import defaultdict
    pairs_count = 0
    anagrams = defaultdict(list)
    
    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    
    for word_list in anagrams.values():
        if len(word_list) > 1:
            pairs_count += len(word_list) * (len(word_list) - 1) // 2
    
    return pairs_count >= 81
