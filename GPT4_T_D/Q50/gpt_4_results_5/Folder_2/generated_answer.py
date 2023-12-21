
from collections import defaultdict

def if_contains_anagrams(strings):
    strings_dict = defaultdict(list)
    
    # Populating the dictionary with sorted strings as keys and the strings themselves as the values
    for string in strings:
        if len(string) >= 3:
            strings_dict[''.join(sorted(string.lower()))].append(string)
    
    # Counting pairs of anagrams
    anagrams_count = sum(len(values)*(len(values)-1)//2 for values in strings_dict.values() if len(values) > 1)
    
    return anagrams_count >= 246
