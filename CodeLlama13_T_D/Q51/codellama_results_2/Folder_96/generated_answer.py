
def if_contains_anagrams(strings):
    anagram_pairs = []
    for i in range(len(strings)):
        s1 = strings[i].lower()
        for j in range(i+1, len(strings)):
            s2 = strings[j].lower()
            if sorted(s1) == sorted(s2):
                anagram_pairs.append((s1, s2))
    return len(anagram_pairs) <= 2 and all(len(s1) >= 3 for s1, _ in anagram_pairs)
