
def if_contains_anagrams(my_list):
    anagram_pairs = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            s1 = my_list[i].lower()
            s2 = my_list[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1) == sorted(s2):
                    anagram_pairs += 1
                    if anagram_pairs > 24:
                        return False
    return True
