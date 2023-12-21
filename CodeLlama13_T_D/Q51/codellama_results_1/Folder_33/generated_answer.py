
def if_contains_anagrams(my_list):
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if (len(set(my_list[i].lower())) >= 3 and len(set(my_list[j].lower())) >= 3) and sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                return True
    return False
