
def if_contains_anagrams(list_of_strings):
    anagram_pairs = []
    for i in range(len(list_of_strings)):
        string1 = list_of_strings[i].lower()
        for j in range(i+1, len(list_of_strings)):
            string2 = list_of_strings[j].lower()
            if len(string1) >= 3 and len(string2) >= 3 and sorted(string1) == sorted(string2):
                anagram_pairs.append((string1, string2))
    return len(anagram_pairs) >= 25
