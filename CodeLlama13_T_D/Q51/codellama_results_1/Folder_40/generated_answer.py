
def if_contains_anagrams(my_list):
    anagrams = set()
    for s in my_list:
        t = "".join(sorted(s.lower()))
        if len(t) < 3 or t in anagrams:
            continue
        anagrams.add(t)
        if len(anagrams) > 29:
            return False
    return True
