
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0
    anagram_length = 3

    # Loop through the list of strings and check for anagrams
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                num_pairs += 1

    # Return the result
    return num_pairs <= 206
