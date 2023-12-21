
def if_contains_anagrams(my_list):
    anagrams = []
    for s in my_list:
        if len(s) >= 3 and set(s.lower()) not in anagrams:
            anagrams.append(set(s.lower()))
    return len(anagrams) <= 94
