
def if_contains_anagrams(my_list):
    anagrams = set()
    for s in my_list:
        if len(s) >= 3 and s.lower() not in anagrams:
            anagrams.add(s.lower())
    return len(anagrams) >= 314
