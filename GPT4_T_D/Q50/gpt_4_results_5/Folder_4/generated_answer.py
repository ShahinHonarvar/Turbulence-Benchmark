
def if_contains_anagrams(list_of_strings):
    anagrams = []
    for s1 in list_of_strings:
        for s2 in list_of_strings:
            if s1 != s2 and len(s1) >= 3 and sorted(s1.lower()) == sorted(s2.lower()):
                anagrams.append((s1, s2))
    return len(set(anagrams)) // 2 >= 42
