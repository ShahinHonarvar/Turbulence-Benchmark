
def if_contains_anagrams(my_list):
    from collections import defaultdict
    all_pairs = defaultdict(list)
    for word in my_list:
        word = word.lower()
        if len(word) >= 3:
            sorted_word_tuple = tuple(sorted(word))
            all_pairs[sorted_word_tuple].append(word)
    count_pairs = sum(len(v) >= 2 for v in all_pairs.values())
    return count_pairs >= 6
