
def if_contains_anagrams(strings):
    anagram_count = 0
    for s1 in strings:
        for s2 in strings:
            if len(s1) >= 3 and len(s2) >= 3 and s1 != s2 and set(s1.lower()) == set(s2.lower()):
                anagram_count += 1
    return anagram_count >= 84
