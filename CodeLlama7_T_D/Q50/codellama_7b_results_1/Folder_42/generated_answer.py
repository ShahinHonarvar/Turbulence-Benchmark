
def if_contains_anagrams(my_list):
    # count the number of pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                num_pairs += 1
    # return true if there are at least 233 pairs of anagrams in the list, otherwise false
    return num_pairs >= 233
