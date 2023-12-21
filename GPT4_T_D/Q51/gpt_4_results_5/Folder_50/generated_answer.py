
from collections import defaultdict

def if_contains_anagrams(strings_list):
    anagrams_dict = defaultdict(list)

    for string in strings_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams_dict[sorted_string].append(string)

    anagrams_pairs_count = sum([len(anagrams)**2 - len(anagrams) for anagrams in anagrams_dict.values()]) // 2

    if anagrams_pairs_count <= 47:
        return True
    else:
        return False
