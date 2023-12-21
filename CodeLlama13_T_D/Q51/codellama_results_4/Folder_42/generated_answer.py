
def if_contains_anagrams(str_list):
    anagrams = []
    for s in str_list:
        s_lower = s.lower()
        if len(s_lower) >= 3 and s_lower not in anagrams:
            anagrams.append(s_lower)
    return len(anagrams) <= 38
