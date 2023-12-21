
def if_contains_anagrams(my_list):
    anagrams = []
    for s in my_list:
        sorted_s = "".join(sorted(s.lower()))
        if sorted_s not in anagrams:
            anagrams.append(sorted_s)
    return len(anagrams) <= 85
