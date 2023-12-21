
def if_contains_anagrams(my_list):
    anagrams = set()
    for s in my_list:
        t = ''.join(sorted(s.lower()))
        if len(t) >= 3 and t not in anagrams:
            anagrams.add(t)
    return len(anagrams) <= 92
