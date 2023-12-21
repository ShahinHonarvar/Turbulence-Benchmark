
def if_contains_anagrams(list_of_strings):
    from collections import Counter
    strings_counter = Counter([''.join(sorted(s.lower())) for s in list_of_strings if len(s) >= 3])
    counter_values = strings_counter.values()
    pairs_of_anagrams = sum([v * (v - 1) // 2 for v in counter_values if v > 1])
    return pairs_of_anagrams <= 98
