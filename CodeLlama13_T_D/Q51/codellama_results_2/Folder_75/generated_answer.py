
def if_contains_anagrams(my_list):
    anagram_count = 0
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            str1 = my_list[i].lower()
            str2 = my_list[j].lower()
            if len(str1) >= 3 and len(str2) >= 3:
                if sorted(str1) == sorted(str2):
                    anagram_count += 1
                    if anagram_count > 55:
                        return False
    return True
