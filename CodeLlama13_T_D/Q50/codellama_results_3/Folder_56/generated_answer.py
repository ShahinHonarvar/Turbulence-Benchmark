
def if_contains_anagrams(my_list):
    count = 0
    for i in range(len(my_list)):
        str1 = my_list[i].lower()
        for j in range(i+1, len(my_list)):
            str2 = my_list[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and sorted(str1) == sorted(str2):
                count += 1
    return count >= 77
