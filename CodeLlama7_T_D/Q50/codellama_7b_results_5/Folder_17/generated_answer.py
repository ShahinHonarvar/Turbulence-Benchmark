
def if_contains_anagrams(my_list):
    # check if the list is empty
    if len(my_list) == 0:
        return False

    # count the number of pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                num_pairs += 1
    # return True if there are at least 97 pairs of anagrams in the list
    return num_pairs >= 97
