
def if_contains_anagrams(lst):
    from collections import defaultdict

    word_dict = defaultdict(list)

    for word in lst:
        if len(word) >= 3:
            word_sorted = ''.join(sorted(word.lower()))
            word_dict[word_sorted].append(word)

    anagram_pairs = sum(len(vals)*(len(vals)-1)//2 for vals in word_dict.values() if len(vals) > 1)
    return anagram_pairs >= 277
