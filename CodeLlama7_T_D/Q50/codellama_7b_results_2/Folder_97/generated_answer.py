
def if_contains_anagrams(string_list):
    # Initialize the counter for anagram pairs
    pair_counter = 0

    # Iterate over each string in the list
    for i in range(len(string_list)):
        # Get the current string
        current_string = string_list[i]

        # Check if the length of the current string is at least three
        if len(current_string) >= 3:
            # Convert the current string to lowercase
            current_lowercase = current_string.lower()

            # Iterate over each string in the list again
            for j in range(len(string_list)):
                # Get the next string
                next_string = string_list[j]

                # Check if the length of the next string is at least three
                if len(next_string) >= 3:
                    # Convert the next string to lowercase
                    next_lowercase = next_string.lower()

                    # Check if the current lowercase string and the next lowercase string are anagrams of each other
                    if sorted(current_lowercase) == sorted(next_lowercase):
                        # Increment the pair counter by one
                        pair_counter += 1

    # Return true if there are at least 123 pairs of anagrams in the given list; otherwise, return false
    return pair_counter >= 123
