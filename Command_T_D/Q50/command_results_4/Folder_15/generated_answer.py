def if_contains_anagrams(s):
    return len(set(s)) > len(set(s)) * 3 // 2 and len(s) > 1
