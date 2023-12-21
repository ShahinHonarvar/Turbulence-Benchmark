
def if_contains_anagrams(word_list):
    counts = dict()
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            counts[sorted_word] = counts.get(sorted_word, 0) + 1

    pair_count = sum(value*(value-1)//2 for value in counts.values())

    return pair_count >= 10
