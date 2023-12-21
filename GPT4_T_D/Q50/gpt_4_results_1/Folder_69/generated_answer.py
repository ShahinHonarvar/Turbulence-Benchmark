
def if_contains_anagrams(lst):
    from itertools import combinations
    from collections import Counter

    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())

    three_letter_strings = [s for s in lst if len(s) >= 3]
    pairs = list(combinations(three_letter_strings, 2))
    anagrams = [pair for pair in pairs if is_anagram(*pair)]

    return len(anagrams) >= 188
