
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of anagram pairs
    anagram_pair_count = 0

    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Loop through each remaining string in the list
        for j in range(i + 1, len(my_list)):
            # Get the other string
            other_string = my_list[j]

            # Check if the current string and other string are anagrams
            if sorted(current_string.lower()) == sorted(other_string.lower()):
                # Increment the counter for the number of anagram pairs
                anagram_pair_count += 1

                # If there are at least 96 pairs of anagrams, return true
                if anagram_pair_count >= 96:
                    return True
