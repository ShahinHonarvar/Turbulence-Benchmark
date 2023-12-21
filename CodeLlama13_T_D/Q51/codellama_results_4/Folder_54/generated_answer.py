
def if_contains_anagrams(string_list):
    anagram_pairs = []
    for s1 in string_list:
        for s2 in string_list[string_list.index(s1)+1:]:
            if len(set(s1).intersection(s2)) == 3 and sorted(s1) != sorted(s2):
                anagram_pairs.append((s1, s2))
    return len(anagram_pairs) <= 39
