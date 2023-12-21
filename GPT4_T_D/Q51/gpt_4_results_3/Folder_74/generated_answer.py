
def if_contains_anagrams(lst):
    from collections import defaultdict
    def sorted_str(s):
        return ''.join(sorted(s.lower()))

    anagram_dict = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            anagram_dict[sorted_str(s)].append(s)

    pairs = sum(len(lst) * (len(lst) - 1) // 2 for lst in anagram_dict.values())
    return pairs <= 57
