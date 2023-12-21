
def if_contains_anagrams(list_of_strings):
    anagram_pairs = []
    for s1 in list_of_strings:
        s1_lower = s1.lower()
        for s2 in list_of_strings[list_of_strings.index(s1) + 1 :]:
            if s2.lower() == "".join(sorted(s1_lower)):
                anagram_pairs.append((s1, s2))
    return len(anagram_pairs) <= 38
