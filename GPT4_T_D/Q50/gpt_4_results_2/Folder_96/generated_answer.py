
def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list if len(s) >= 3]
    sorted_list = [''.join(sorted(s)) for s in str_list]
    counts = {}
    for s in sorted_list:
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1
    anagram_pairs = sum(c*(c-1)//2 for c in counts.values())
    return anagram_pairs >= 98
