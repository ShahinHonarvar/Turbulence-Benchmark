
def if_contains_anagrams(lst):
    from collections import defaultdict

    def signature(word):
        return ''.join(sorted(word.lower()))

    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_dict[signature(word)].append(word)

    count = sum(len(lst) * (len(lst) - 1) // 2 for lst in anagram_dict.values() if len(lst)>1)

    return count >= 42
