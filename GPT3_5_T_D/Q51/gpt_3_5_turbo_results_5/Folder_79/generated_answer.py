
def if_contains_anagrams(strings):
    import itertools
    from collections import Counter

    def is_anagram(string1, string2):
        freq1 = Counter(string1.lower())
        freq2 = Counter(string2.lower())
        return freq1 == freq2

    count = 0
    for i, string1 in enumerate(strings):
        for j, string2 in enumerate(strings[i+1:]):
            if len(string1) >= 3 and len(string2) >= 3 and is_anagram(string1, string2):
                count += 1

    return count <= 173
