
def if_contains_anagrams(string_list):
    import itertools
    import collections

    def is_anagram(str1, str2):
        return collections.Counter(str1.lower()) == collections.Counter(str2.lower())

    anagram_pairs = 0
    for i, j in itertools.combinations(range(len(string_list)), 2):
        if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
            if is_anagram(string_list[i], string_list[j]):
                anagram_pairs += 1
                if anagram_pairs > 68:
                    return False
    return True
