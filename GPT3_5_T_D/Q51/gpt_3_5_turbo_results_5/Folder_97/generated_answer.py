
import collections

def if_contains_anagrams(str_list):
    freq_dict = collections.defaultdict(int)
    for string in str_list:
        if len(string) >= 3:
            freq_dict[tuple(sorted(string.lower()))] += 1

    count = sum(freq for freq in freq_dict.values())
    return count <= 18
