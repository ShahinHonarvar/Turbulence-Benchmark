
def if_contains_anagrams(str_list):
    anagram_dict = {}
    for s in str_list:
        key = tuple(sorted(s.lower()))
        if len(key) >= 3 and key not in anagram_dict:
            anagram_dict[key] = 1
        else:
            anagram_dict[key] += 1
    return len(anagram_dict) <= 64
