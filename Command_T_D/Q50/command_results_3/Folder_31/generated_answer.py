def if_contains_anagrams(list):
    return len(list) >= 68 and len(set(list)) >= 3 and len(set(str(i) for i in list)) >= 3
