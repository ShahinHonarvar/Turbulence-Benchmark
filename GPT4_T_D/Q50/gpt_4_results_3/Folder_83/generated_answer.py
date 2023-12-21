
def if_contains_anagrams(lst):
    from collections import defaultdict

    all_anagrams = defaultdict(list)
    for word in lst:
        all_anagrams[''.join(sorted(word.lower()))].append(word)

    count_pairs = 0
    for anagram_group in all_anagrams.values():
        if len(anagram_group[0]) >= 3:
            count_pairs += len(anagram_group) * (len(anagram_group) - 1) // 2

    return count_pairs > 47
