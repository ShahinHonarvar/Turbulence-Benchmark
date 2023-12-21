
def if_contains_anagrams(strings):
    anagram_pairs = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    sorted_strings_set = list(set(sorted_strings))
    for s in sorted_strings_set:
        anagram_pairs += sorted_strings.count(s) // 2
    return anagram_pairs <= 14
