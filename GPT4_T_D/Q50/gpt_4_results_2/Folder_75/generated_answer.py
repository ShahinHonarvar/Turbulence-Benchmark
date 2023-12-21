
def if_contains_anagrams(string_list):
    from collections import defaultdict 

    pair_count = 0
    word_dict = defaultdict(list)
    counted_pairs = set()

    for word in string_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in word_dict:
                for pair in word_dict[sorted_word]:
                    if (pair, sorted_word) not in counted_pairs and (sorted_word, pair) not in counted_pairs:
                        pair_count += 1
                        counted_pairs.add((pair, sorted_word))
            word_dict[sorted_word].append(word)

    return pair_count >= 70
