
def if_contains_anagrams(lst):
    anagram_dict = {}
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s_lower)
            else:
                anagram_dict[sorted_s] = [s_lower]
    
    counter = 0
    for vals in anagram_dict.values():
        if len(vals) > 1:
            counter += 1
            if counter > 5:
                return False
    return True
