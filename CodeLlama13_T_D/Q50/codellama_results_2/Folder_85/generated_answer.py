
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for i in range(len(strings)):
        string1 = strings[i].lower()
        for j in range(i + 1, len(strings)):
            string2 = strings[j].lower()
            if len(string1) >= 3 and len(string2) >= 3:
                anagram_pairs += 1 if sorted(string1) == sorted(string2) else 0
    return anagram_pairs >= 73
