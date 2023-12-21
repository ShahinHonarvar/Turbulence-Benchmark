
def if_contains_anagrams(my_list):
    # check if the list is empty
    if len(my_list) == 0:
        return False

    # count the number of anagrams in the list
    num_anagrams = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j]):
                num_anagrams += 1
    # check if the number of anagrams is at most 17
    return num_anagrams <= 17
