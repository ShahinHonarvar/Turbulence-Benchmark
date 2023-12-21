
def if_contains_anagrams(str_list):
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if len(set(str_list[i].lower())) >= 3 and len(set(str_list[j].lower())) >= 3:
                if set(str_list[i].lower()) == set(str_list[j].lower()):
                    return True
    return False
