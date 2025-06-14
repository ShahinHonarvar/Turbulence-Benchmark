
def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for i in range(len(list_of_strings)):
        string1 = list_of_strings[i].lower()
        for j in range(i+1, len(list_of_strings)):
            string2 = list_of_strings[j].lower()
            if len(string1) >= 3 and len(string2) >= 3:
                anagram = "".join(sorted(string1)) == "".join(sorted(string2))
                if anagram:
                    anagram_pairs += 1
    return anagram_pairs >= 189
