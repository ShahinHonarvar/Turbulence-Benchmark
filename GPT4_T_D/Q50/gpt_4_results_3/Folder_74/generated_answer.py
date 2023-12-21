
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagrams = defaultdict(list)

    def sorted_str(s):
        return "".join(sorted(s.lower()))

    # Populate anagram groups.
    for s in lst:
        if len(s) >= 3:
            anagrams[sorted_str(s)].append(s)

    # Count anagram pairs.
    pairs_count = sum(len(val) * (len(val) - 1) // 2 for val in anagrams.values())

    return pairs_count >= 17
