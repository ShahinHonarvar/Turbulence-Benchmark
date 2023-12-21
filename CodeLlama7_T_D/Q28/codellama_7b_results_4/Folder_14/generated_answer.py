
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the indices of the characters in the specified range
    start_index = 46
    end_index = 82
    # Initialize a dictionary to store the character counts
    char_counts = {}

    # Iterate over the characters in the list and count their occurrences
    for char in char_list:
        if char not in char_counts:
            char_counts[char] = 1

        else:

            char_counts[char] += 1

    # Sort the dictionary by value (the count) and grab the 16th smallest value
    sorted_counts = sorted(char_counts.items(), key=lambda x: x[1])
    smallest_value = sorted_counts[0][1]
    nth_smallest_value = sorted_counts[15][1]
    # Return the character with the 16th smallest ASCII value among those characters in the string that occur between indices 46 to 82, both inclusive
    return char_list[nth_smallest_value - smallest_value + start_index]
