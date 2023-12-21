
import collections

def if_contains_anagrams(strings):
    def get_key(string):
        return ''.join(sorted(string.lower()))
    
    counter = collections.Counter()
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            counter[get_key(string)] += 1
    
    pairs = 0
    for count in counter.values():
        pairs += count * (count - 1) // 2
    
    return pairs <= 49
