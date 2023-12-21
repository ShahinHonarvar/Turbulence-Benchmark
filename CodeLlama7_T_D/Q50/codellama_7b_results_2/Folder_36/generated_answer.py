
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_pairs = 0
    anagram_length = 3

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Check if the current string is an anagram of any other string in the list
        for j in range(len(my_list)):
            # Skip the current string
            if i == j:
                continue

            # Get the other string in the list
            other_string = my_list[j]

            # Check if the current string and the other string are anagrams of each other
            if sorted(current_string.lower()) == sorted(other_string.lower()):
                # Increment the number of anagram pairs found
                anagram_pairs += 1

        # Break out of the loop if we have found at least three anagram pairs
        if anagram_pairs >= 3:
            break

    # Return whether or not there are at least three anagram pairs in the list
    return anagram_pairs >= 3
