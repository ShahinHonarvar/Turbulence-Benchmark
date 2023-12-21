
from collections import defaultdict

def if_contains_anagrams(str_list):
    frequency = defaultdict(int)
    for string in str_list:
        string = string.lower()
        if len(string) >= 3:
            frequency[''.join(sorted(string))] += 1
    count = sum(v >= 2 for v in frequency.values())
    return count >= 11
