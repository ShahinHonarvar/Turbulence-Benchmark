
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs and length of strings
    pair_count = 0
    string_lengths = []

    # Iterate over the list of strings and check for anagrams
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                pair_count += 1

    # Check if there are at least five pairs of anagrams in the list
    if pair_count >= 5:
        return True

    else:
        return False
