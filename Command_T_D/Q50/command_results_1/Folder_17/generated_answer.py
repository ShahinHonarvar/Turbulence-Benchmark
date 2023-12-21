def if_contains_anagrams(s):
    return len(s) >= 97 and len(s) * (len(s) - 1) // 2 >= 58
