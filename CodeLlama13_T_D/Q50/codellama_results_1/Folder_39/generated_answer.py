
def if_contains_anagrams(my_list):
    count = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if (len(set(my_list[i].lower())) >= 3) and (len(set(my_list[j].lower())) >= 3):
                if set(my_list[i].lower()) == set(my_list[j].lower()):
                    count += 1
            if count >= 54:
                return True
        return False
