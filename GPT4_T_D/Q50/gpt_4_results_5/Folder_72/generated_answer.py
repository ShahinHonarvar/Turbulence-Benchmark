
def if_contains_anagrams(lst):
    from collections import defaultdict

    words_by_sorted_tuple = defaultdict(list)

    for word in lst:
        if len(word) >= 3:
            key = tuple(sorted(word.lower()))
            words_by_sorted_tuple[key].append(word)

    pairs = 0
    for word_list in words_by_sorted_tuple.values():
        num_words = len(word_list)
        if num_words > 1:
            pairs += num_words * (num_words - 1) // 2
        if pairs >= 55:
            return True
    return False
