
def if_contains_anagrams(lst):
    from collections import defaultdict
    anagram_dict = defaultdict(list)
    
    # build anagram dictionary
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s].append(s)
    
    pair_count = 0
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            pair_count += len(anagram_list) * (len(anagram_list) - 1) // 2
    
    return pair_count >= 84
