
def if_contains_anagrams(lst):
    def count_anagrams(word, lst):
        count = 0
        for w in lst:
            if len(w) >= 3 and word.lower() != w.lower() and sorted(word.lower()) == sorted(w.lower()):
                count += 1
        return count

    pair_count = 0
    for i, word in enumerate(lst):
        pair_count += count_anagrams(word, lst[i + 1:])

    return pair_count >= 312
