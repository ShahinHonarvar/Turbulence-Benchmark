
def if_contains_anagrams(str_list):
    from collections import defaultdict
    anagrams = defaultdict(list)

    for string in str_list:
        anagrams[''.join(sorted(string.lower()))].append(string)

    pairs = sum(len(c) * (len(c) - 1) // 2 for c in anagrams.values() if len(c[0]) >= 3)

    return pairs >= 246
