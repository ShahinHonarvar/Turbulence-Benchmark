
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the number of anagrams in the list
    num_anagrams = 0

    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                num_anagrams += 1

    # Check if there are more than four anagrams in the list
    return num_anagrams <= 46
