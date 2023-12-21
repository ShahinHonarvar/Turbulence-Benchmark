
def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    freq_dict = {}
    for s in sorted_strings:
        if s in freq_dict:
            freq_dict[s] += 1
        else:
            freq_dict[s] = 1
    pairs = sum(f*(f-1)//2 for f in freq_dict.values())
    return pairs >= 34
