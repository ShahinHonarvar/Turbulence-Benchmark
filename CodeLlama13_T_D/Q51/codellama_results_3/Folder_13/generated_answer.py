
def if_contains_anagrams(my_list):
    anagram_pairs = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            s1 = my_list[i].lower()
            s2 = my_list[j].lower()
            if (len(s1) >= 3 and len(s2) >= 3) and sorted(s1) == sorted(s2):
                anagram_pairs += 1
    return anagram_pairs <= 54
