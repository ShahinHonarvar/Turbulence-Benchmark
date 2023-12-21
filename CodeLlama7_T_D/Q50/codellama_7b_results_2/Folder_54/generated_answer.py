
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs
    pair_count = 0
    length_threshold = 3

    # Iterate over the list of strings and check for anagrams
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                pair_count += 1

    # Return True if there are at least 74 pairs of anagrams, False otherwise
    return pair_count >= 74
