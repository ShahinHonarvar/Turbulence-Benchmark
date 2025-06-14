
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Initialize a dictionary to store the ASCII values and their counts
    ascii_counts = {}

    # Iterate over the characters in the list
    for char in char_list:
        # Get the ASCII value of the current character
        ascii_value = ord(char)

        # If the ASCII value is not already in the dictionary, add it with a count of 1
        if ascii_value not in ascii_counts:
            ascii_counts[ascii_value] = 1

        # Otherwise, increment the count for the current ASCII value
        else:
            ascii_counts[ascii_value] += 1

    # Sort the dictionary by key (ASCII value)
    sorted_ascii_counts = sorted(ascii_counts.items(), key=lambda x: x[0])

    # Get the 8th smallest ASCII value from the sorted dictionary
    nth_smallest_ascii_value = sorted_ascii_counts[7][0]

    # Return the character with that ASCII value
    return chr(nth_smallest_ascii_value)
