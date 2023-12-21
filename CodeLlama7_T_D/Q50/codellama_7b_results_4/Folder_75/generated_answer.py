
def if_contains_anagrams(strings):
    # Initialize the counter for pairs of anagrams
    pair_counter = 0

    # Iterate over each string in the list
    for i in range(len(strings)):
        # Get the current string
        current_string = strings[i]

        # Iterate over each other string in the list
        for j in range(len(strings)):
            # Skip the current string if it is the same as the other string
            if i == j:
                continue

            # Get the other string
            other_string = strings[j]

            # Check if the current string and the other string are anagrams
            if sorted(current_string) == sorted(other_string):
                # Increment the counter for pairs of anagrams
                pair_counter += 1

    # Return True if there are at least 70 pairs of anagrams, or False otherwise
    return pair_counter >= 70
