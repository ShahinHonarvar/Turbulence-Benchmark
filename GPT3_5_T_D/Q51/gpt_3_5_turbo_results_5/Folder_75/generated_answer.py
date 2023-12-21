
import collections

def if_contains_anagrams(string_list):
    counts = collections.Counter()
    anagram_count = 0

    for string in string_list:
        string = string.lower()
        if len(string) >= 3:
            counts[tuple(sorted(string))] += 1

    for count in counts.values():
        anagram_count += count * (count - 1) // 2

    return anagram_count <= 55
