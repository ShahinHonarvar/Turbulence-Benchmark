
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s1 in strings:
        for s2 in strings:
            if s1.lower() == s2.lower():
                continue
            if len(s1) < 3 or len(s2) < 3:
                continue
            if sorted(s1) == sorted(s2):
                anagram_pairs += 1
    return anagram_pairs <= 116
