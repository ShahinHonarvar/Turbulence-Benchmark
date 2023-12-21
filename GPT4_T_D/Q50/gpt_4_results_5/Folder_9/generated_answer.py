
from collections import defaultdict

def if_contains_anagrams(strings):
    strings_frequency = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            strings_frequency[''.join(sorted(string.lower()))] += 1
    pairs = sum(freq // 2 for freq in strings_frequency.values())
    return pairs >= 66
