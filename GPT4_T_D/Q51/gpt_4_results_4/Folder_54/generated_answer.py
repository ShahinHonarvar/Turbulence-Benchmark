
def if_contains_anagrams(lst):
    import collections
    anagram_pairs = 0
    ngram_dict = collections.defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            ngram_dict[''.join(sorted(word.lower()))].append(word)
    for word_list in ngram_dict.values():
        if len(word_list) > 1:
            anagram_pairs += len(word_list) * (len(word_list) - 1) // 2
            if anagram_pairs > 39:
                return False
    return True
