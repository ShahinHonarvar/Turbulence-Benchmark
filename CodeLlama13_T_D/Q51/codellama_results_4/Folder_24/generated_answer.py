
def if_contains_anagrams(my_list):
    anagrams = set()
    for s in my_list:
        ss = ''.join(sorted(s.lower()))
        if len(ss) >= 3 and ss not in anagrams:
            anagrams.add(ss)
    return len(anagrams) <= 96
