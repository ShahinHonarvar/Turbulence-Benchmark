
def if_contains_anagrams(lst):
    freq_map = {}
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            if sorted_s in freq_map:
                freq_map[sorted_s] += 1
            else:
                freq_map[sorted_s] = 1
    return len([k for k, v in freq_map.items() if v >= 2]) >= 4
