
def if_contains_anagrams(my_list):
    # Iterate through the list of strings and check for anagrams
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                return True
    return False
