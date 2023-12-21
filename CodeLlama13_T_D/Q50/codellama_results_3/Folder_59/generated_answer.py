
def if_contains_anagrams(strings):
    anagrams = []
    for i in range(len(strings)):
        string1 = strings[i].lower()
        for j in range(i + 1, len(strings)):
            string2 = strings[j].lower()
            if len(string1) >= 3 and len(string2) >= 3 and sorted(string1) == sorted(string2):
                anagrams.append((string1, string2))
    return len(anagrams) >= 10
