
def if_contains_anagrams(lst):
    from collections import Counter
    pairs = 0
    word_dict = {"".join(sorted(word.lower())) : [] for word in lst if len(word) >= 3}
    for word in lst:
        sorted_word = "".join(sorted(word.lower()))
        if sorted_word in word_dict and len(word) >= 3:
            pairs += len(word_dict[sorted_word])
            word_dict[sorted_word].append(word)
    return pairs >= 79
