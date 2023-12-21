
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
    count_pairs = sum([Counter(strings).most_common(1)[0][1] - 1 for strings in anagrams.values() if Counter(strings).most_common(1)[0][1] > 1])
    return count_pairs >= 55
