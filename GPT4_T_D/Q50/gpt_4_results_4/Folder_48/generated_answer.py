
def if_contains_anagrams(strings_list):
    from collections import Counter
    hashing_words = Counter([''.join(sorted(s.lower())) for s in strings_list if len(s) > 2])
    anagram_pairs = sum(n * (n-1) // 2 for n in hashing_words.values())
    return anagram_pairs >= 219
