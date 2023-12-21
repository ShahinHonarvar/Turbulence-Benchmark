
from collections import defaultdict

def if_contains_anagrams(lst):
    count_dict = defaultdict(list)
    for string in lst:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            count_dict[sorted_str].append(string)
    counter = sum([len(values)*(len(values)-1)//2 for key,values in count_dict.items()])
    return counter <= 257
