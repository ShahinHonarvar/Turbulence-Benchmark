
import collections

def if_contains_anagrams(strings):
    count = 0
    anagrams = collections.defaultdict(int)
    
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string] += 1
        count += anagrams[sorted_string] - 1
    
    return count >= 312
