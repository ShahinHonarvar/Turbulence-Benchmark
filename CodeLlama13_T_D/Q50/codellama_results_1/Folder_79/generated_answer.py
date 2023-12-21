
def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for string1 in list_of_strings:
        for string2 in list_of_strings:
            if (string1.lower() == string2.lower()) and (len(string1) >= 3) and (len(string2) >= 3):
                anagram_count += 1
    return anagram_count >= 40
