def if_contains_anagrams(str_list):
    return sum(1 for s in str_list if s[0] == s[1] and len(s) >= 3) >= 84
