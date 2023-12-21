
def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for s in string_list:
        s_lower = s.lower()
        for t in string_list[len(s_lower) - 3 :]:
            t_lower = t.lower()
            if len(t_lower) >= 3 and set(s_lower) == set(t_lower):
                anagram_pairs += 1
    return anagram_pairs <= 64
