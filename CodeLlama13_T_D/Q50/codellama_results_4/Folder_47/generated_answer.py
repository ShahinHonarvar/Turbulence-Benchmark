
def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    for i in range(len(list_of_strings)):
        str1 = list_of_strings[i].lower()
        for j in range(i+1, len(list_of_strings)):
            str2 = list_of_strings[j].lower()
            if len(str1) >= 3 and len(str2) >= 3:
                if sorted(str1) == sorted(str2):
                    anagram_count += 1
                    if anagram_count >= 47:
                        return True
    return False
