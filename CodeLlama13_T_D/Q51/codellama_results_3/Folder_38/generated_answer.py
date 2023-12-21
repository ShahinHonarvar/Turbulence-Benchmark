
def if_contains_anagrams(str_list):
    anagrams = set()
    for s in str_list:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3 and key not in anagrams:
            anagrams.add(key)
    return len(anagrams) <= 416
