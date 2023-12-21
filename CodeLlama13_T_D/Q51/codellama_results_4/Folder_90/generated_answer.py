
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s1 in strings:
        for s2 in strings:
            if s1 != s2 and len(s1) >= 3 and len(s2) >= 3:
                sorted_s1 = "".join(sorted(s1.lower()))
                sorted_s2 = "".join(sorted(s2.lower()))
                if sorted_s1 == sorted_s2:
                    anagram_pairs += 1
    return anagram_pairs <= 147
