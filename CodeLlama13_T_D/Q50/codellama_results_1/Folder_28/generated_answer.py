
def if_contains_anagrams(my_list):
    anagrams = []
    for i in range(len(my_list)):
        string1 = my_list[i].lower()
        for j in range(i + 1, len(my_list)):
            string2 = my_list[j].lower()
            if sorted(string1) == sorted(string2):
                anagrams.append((i, j))
    return len(anagrams) >= 81
