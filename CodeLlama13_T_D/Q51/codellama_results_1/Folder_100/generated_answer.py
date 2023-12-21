
def if_contains_anagrams(my_list):
    anagram_count = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            s1 = my_list[i].lower()
            s2 = my_list[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                s1_sorted = "".join(sorted(s1))
                s2_sorted = "".join(sorted(s2))
                if s1_sorted == s2_sorted:
                    anagram_count += 1
            if anagram_count > 98:
                return False
    return True
