
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Check if the current string is an anagram of another string in the list
        for j in range(len(my_list)):
            # Skip the same index as the outer loop
            if i == j:
                continue

            # Get the other string in the list
            other_string = my_list[j]

            # Check if the current string and the other string are anagrams of each other
            if sorted(current_string.lower()) == sorted(other_string.lower()):
                # Increment the counter for the number of anagrams found
                num_anagrams += 1

    # Return True if there are at most 40 pairs of anagrams in the given list, otherwise return False
    return num_anagrams <= 40
