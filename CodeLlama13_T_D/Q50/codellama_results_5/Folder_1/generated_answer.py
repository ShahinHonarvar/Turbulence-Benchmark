
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        s1 = strings[i].lower()
        for j in range(i + 1, len(strings)):
            s2 = strings[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1) == sorted(s2):
                    anagram_pairs += 1
    return anagram_pairs >= 96
