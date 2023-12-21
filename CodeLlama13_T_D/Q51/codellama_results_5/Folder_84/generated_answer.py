
def if_contains_anagrams(list_of_strings):
    anagram_pairs = []
    for i in range(len(list_of_strings)):
        str1 = list_of_strings[i].lower()
        for j in range(i+1, len(list_of_strings)):
            str2 = list_of_strings[j].lower()
            if sorted(str1) == sorted(str2):
                anagram_pairs.append((str1, str2))
    return len(anagram_pairs) <= 16
