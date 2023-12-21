
from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)

    for word in strings:
        anagram_dict[''.join(sorted(word.lower()))].append(word)

    count = 0
    for values in anagram_dict.values():
        if len(values) > 1:
            count += len(values) * (len(values) - 1) / 2

    return count <= 67
