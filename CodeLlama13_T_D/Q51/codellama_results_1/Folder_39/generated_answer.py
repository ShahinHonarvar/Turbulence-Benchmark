
def if_contains_anagrams(my_list):
    anagram_count = 0
    for i in range(len(my_list)):
        s1 = my_list[i].lower()
        for j in range(i+1, len(my_list)):
            s2 = my_list[j].lower()
            if sorted(s1) == sorted(s2):
                anagram_count += 1
    return anagram_count <= 257
