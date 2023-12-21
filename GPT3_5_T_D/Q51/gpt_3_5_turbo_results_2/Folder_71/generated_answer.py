
import collections

def if_contains_anagrams(string_list):
    counter = collections.Counter()
    pairs = 0
    
    for string in string_list:
        if len(string) >= 3 and string.isalpha():
            counter[tuple(sorted(string.lower()))] += 1
    
    for key in counter:
        count = counter[key]
        pairs += count * (count - 1) // 2
        
    return pairs <= 9
