
def if_contains_anagrams(input_list):
    from collections import defaultdict

    def frozenset_from_string(string):
        return frozenset(string.lower())

    def is_anagram(string1, string2):
        return frozenset_from_string(string1) == frozenset_from_string(string2)

    string_set = defaultdict(list)

    for s in input_list:
        if len(s) >= 3:
            string_set[frozenset_from_string(s)].append(s)

    pairs_count = sum([len(val_list) * (len(val_list) - 1) // 2 for val_list in string_set.values()])

    return pairs_count >= 115
