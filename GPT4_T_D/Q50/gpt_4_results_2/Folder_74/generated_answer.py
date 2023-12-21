
def if_contains_anagrams(lst):
    from collections import defaultdict

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    d = defaultdict(list)

    for word in lst:
        if len(word) >= 3:
            d[tuple(sorted(word.lower()))].append(word)

    anagram_pairs = sum(len(v)*(len(v)-1)/2 for v in d.values())

    return anagram_pairs >= 17
