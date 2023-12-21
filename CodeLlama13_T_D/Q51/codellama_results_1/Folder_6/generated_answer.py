
def if_contains_anagrams(my_list):
    count = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            s1 = my_list[i].lower()
            s2 = my_list[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1) == sorted(s2):
                    count += 1
    return count <= 86
