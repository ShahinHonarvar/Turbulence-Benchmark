
def if_contains_anagrams(my_list):
    # Define the length of the anagram
    anagram_length = 3

    # Create a counter variable to keep track of the number of pairs of anagrams found
    pair_counter = 0

    # Iterate through the list and check for anagrams of at least three characters
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            # Check if the strings are anagrams by comparing their sorted forms
            if sorted(my_list[i]) == sorted(my_list[j]):
                # If they are anagrams, increment the pair counter
                pair_counter += 1

    # Return true if there are at least 70 pairs of anagrams in the list; otherwise return false
    return pair_counter >= 70
