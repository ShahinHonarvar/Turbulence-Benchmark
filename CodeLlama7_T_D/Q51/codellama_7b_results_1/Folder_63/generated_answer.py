
def if_contains_anagrams(my_list):
    # Calculate the number of anagram pairs in the list
    num_pairs = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                num_pairs += 1
    # Return True if the number of anagram pairs is at most 423, False otherwise
    return num_pairs <= 423
