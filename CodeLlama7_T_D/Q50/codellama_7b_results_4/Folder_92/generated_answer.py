
def if_contains_anagrams(my_list):
    # check if there are at least two pairs of anagrams in the list
    for i in range(len(my_list) - 1)):
        for j in range(i + 1, len(my_list))):
            # check if the strings are anagrams
            if sorted(my_list[i]) == sorted(my_list[j])):
                # count the number of pairs of anagrams
                num_anagrams += 1
                if num_anagrams >= 2:
                    return True
