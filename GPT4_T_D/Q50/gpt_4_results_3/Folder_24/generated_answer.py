
def if_contains_anagrams(lst):
    from collections import defaultdict

    word_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            word_dict[''.join(sorted(word.lower()))].append(word)

    anagram_pairs = 0
    for values in word_dict.values():
        n = len(values)
        anagram_pairs += (n * (n - 1)) // 2

    return anagram_pairs >= 65
