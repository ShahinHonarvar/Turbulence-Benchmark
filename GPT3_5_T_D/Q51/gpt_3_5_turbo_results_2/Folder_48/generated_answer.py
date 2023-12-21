
import collections

def if_contains_anagrams(my_list):
    def is_valid(string):
        return len(string) >= 3 and string.isalpha()
    
    def get_key(string):
        return tuple(sorted(string.lower()))
    
    counter = collections.Counter()
    for string in my_list:
        if is_valid(string):
            counter[get_key(string)] += 1
    
    pairs_of_anagrams = sum(count * (count - 1) // 2 for count in counter.values())
    return pairs_of_anagrams <= 277
