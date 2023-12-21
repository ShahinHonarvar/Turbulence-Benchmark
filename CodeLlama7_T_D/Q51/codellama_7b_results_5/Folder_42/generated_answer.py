
def if_contains_anagrams(my_list):
    # Count the number of anagrams in the list
    num_anagrams = 0
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                num_anagrams += 1
                if num_anagrams > 38:
                    return False

    return True
