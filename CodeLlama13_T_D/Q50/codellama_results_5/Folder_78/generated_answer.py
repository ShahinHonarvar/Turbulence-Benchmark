
def if_contains_anagrams(my_list):
    anagrams = []
    for s1 in my_list:
        for s2 in my_list[my_list.index(s1) + 1 :]:
            if len(s1) >= 3 and len(s2) >= 3 and sorted(s1.lower()) == sorted(s2.lower()):
                anagrams.append((s1, s2))
    return len(anagrams) >= 79
