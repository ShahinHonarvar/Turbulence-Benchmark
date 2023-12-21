
def if_contains_anagrams(string_list):
    anagrams = []
    for s1 in string_list:
        for s2 in string_list[string_list.index(s1) + 1:]:
            if sorted(s1.lower()) == sorted(s2.lower()):
                anagrams.append((s1, s2))
    return len(anagrams) >= 9
