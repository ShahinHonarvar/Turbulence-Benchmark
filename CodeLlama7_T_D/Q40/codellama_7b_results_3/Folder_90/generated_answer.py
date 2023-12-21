
def return_n_smallest_chars(string, n=24):
    # Create a dictionary to store the character counts
    char_counts = {}

    # Loop through each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count
        if char in char_counts:
            char_counts[char] += 1
        # Otherwise, add it to the dictionary with a count of 1
        else:
            char_counts[char] = 1

    # Sort the dictionary by value (descending) and create a list of characters
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the first n characters of the list, where n is the number of characters to return
    return [char for char, count in sorted_chars[:n]]
