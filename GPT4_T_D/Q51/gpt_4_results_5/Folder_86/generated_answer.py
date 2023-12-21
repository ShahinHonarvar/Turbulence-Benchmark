
def if_contains_anagrams(lst):
    from collections import Counter
    counter = Counter([''.join(sorted(word.lower())) for word in lst if len(word) >= 3])
    anagram_pairs_count = sum(v * (v - 1) // 2 for v in counter.values())
    return anagram_pairs_count <= 48
