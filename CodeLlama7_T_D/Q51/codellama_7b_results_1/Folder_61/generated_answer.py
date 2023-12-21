
def if_contains_anagrams(my_list):
    # Count the number of anagrams in the list
    num_anagrams = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                num_anagrams += 1
    # If there are more than 50 pairs of anagrams in the list, return False
    if num_anagrams > 50:
        return False

    # Otherwise, return True

    else:

        return True
