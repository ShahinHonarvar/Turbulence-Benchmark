
def if_contains_anagrams(lst):
    from collections import Counter
    pairs_counter = 0
    str_counter = ["".join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counter_data = Counter(str_counter)
    for word in counter_data:
        pairs_counter += counter_data[word] // 2
    return pairs_counter >= 43
