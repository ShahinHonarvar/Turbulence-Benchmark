
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)
    pairs_count = sum(len(value) * (len(value) - 1) // 2 for key, value in anagram_dict.items())
    return pairs_count >= 49
