
def if_contains_anagrams(my_list):
    count = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i].lower() == my_list[j].lower():
                count += 1
    return count >= 277
