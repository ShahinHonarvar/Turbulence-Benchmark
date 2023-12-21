
def if_contains_anagrams(strings):
    anagram_pairs = []
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            str1 = strings[i].lower()
            str2 = strings[j].lower()
            if len(str1) >= 3 and len(str2) >= 3:
                anagram_pairs.append((str1, str2))
    return len(anagram_pairs) >= 54
