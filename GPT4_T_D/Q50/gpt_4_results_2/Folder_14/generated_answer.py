
def if_contains_anagrams(lst):
    from collections import defaultdict

    def is_anagram(str_one, str_two):
        return sorted(str_one.lower()) == sorted(str_two.lower())

    pairs = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            pairs[''.join(sorted(word.lower()))].append(word)

    pair_count = sum(len(v) * (len(v) - 1) // 2 for v in pairs.values())
    return pair_count >= 22
