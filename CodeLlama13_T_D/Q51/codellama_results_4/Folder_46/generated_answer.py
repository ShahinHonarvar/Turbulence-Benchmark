
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            s1, s2 = strings[i], strings[j]
            if len(s1) >= 3 and len(s2) >= 3:
                anagram_pairs += int(sorted(s1.lower()) == sorted(s2.lower()))
    return anagram_pairs <= 61
