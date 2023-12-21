
from collections import defaultdict

def if_contains_anagrams(lst):
    sorted_string_list = list(map(lambda string: ''.join(sorted(string.lower())), lst))
    anagrams_dict = defaultdict(list)
    
    for string in sorted_string_list:
        if len(string) >= 3:
            anagrams_dict[string].append(string)

    count_of_anagrams = list(filter(lambda x: len(x) > 1, anagrams_dict.values()))

    pairs = sum([len(sublist) * (len(sublist) - 1) // 2 for sublist in count_of_anagrams])
    
    if pairs <= 21:
        return True
    else:
        return False
