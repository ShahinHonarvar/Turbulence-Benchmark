
def if_contains_anagrams(strings):
    anagram_pairs = []
    for s in strings:
        lowercase_s = s.lower()
        sorted_s = "".join(sorted(lowercase_s))
        if sorted_s not in anagram_pairs:
            anagram_pairs.append(sorted_s)
    return len(anagram_pairs) <= 97
