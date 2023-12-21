
def if_contains_anagrams(my_list):
    # count the number of anagrams in the list
    num_anagrams = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                num_anagrams += 1
                # check if the anagram is at least three characters long
                if len(my_list[i]) >= 3:
                    return True

    # if there are no anagrams in the list, return false

    return False
