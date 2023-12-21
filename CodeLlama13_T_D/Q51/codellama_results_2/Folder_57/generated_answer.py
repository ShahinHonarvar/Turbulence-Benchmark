
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s1 in strings:
        for s2 in strings[strings.index(s1) + 1:]:
            if set(s1.lower()) == set(s2.lower()):
                anagram_pairs += 1
                if anagram_pairs > 74:
                    return False
    return True
