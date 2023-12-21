
def if_contains_anagrams(strings):
    anagram_pairs = []
    for i in range(len(strings)):
        string1 = strings[i].lower()
        for j in range(i+1, len(strings)):
            string2 = strings[j].lower()
            if len(string1) >= 3 and len(string2) >= 3:
                if "".join(sorted(string1)) == "".join(sorted(string2)):
                    anagram_pairs.append((i, j))
    return len(anagram_pairs) <= 42
