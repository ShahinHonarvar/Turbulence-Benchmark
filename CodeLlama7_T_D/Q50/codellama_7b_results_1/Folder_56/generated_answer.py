
def if_contains_anagrams(list_of_strings):
    # Check if the list is empty
    if len(list_of_strings) == 0:
        return False

    # Initialize a counter for the number of anagram pairs
    num_anagram_pairs = 0

    # Iterate over each string in the list
    for i in range(len(list_of_strings)):
        # Get the current string
        current_string = list_of_strings[i]

        # Check if the current string is at least three characters long
        if len(current_string) >= 3:
            # Convert the current string to lowercase for case-insensitive comparison
            lowercase_current_string = current_string.lower()

            # Iterate over each string in the list again, starting from the next string after the current string
            for j in range(i + 1, len(list_of_strings)):
                # Get the current comparison string
                comparison_string = list_of_strings[j]

                # Check if the comparison string is at least three characters long and not equal to the current string
                if len(comparison_string) >= 3 and comparison_string != lowercase_current_string:
                    # Convert the comparison string to lowercase for case-insensitive comparison
                    lowercase_comparison_string = comparison_string.lower()

                    # Check if the current string and the comparison string are anagrams of each other
                    if sorted(lowercase_current_string) == sorted(lowercase_comparison_string):
                        # Increment the counter for the number of anagram pairs
                        num_anagram_pairs += 1

    # Return True if there are at least 77 pairs of anagrams in the given list, or False otherwise
    return num_anagram_pairs >= 77
