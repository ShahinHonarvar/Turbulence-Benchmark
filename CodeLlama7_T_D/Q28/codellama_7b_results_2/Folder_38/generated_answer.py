
def return_nth_smallest_ascii(string):
    # Initialize a dictionary to keep track of the ASCII values and their frequencies
    ascii_values = {}

    # Iterate through the string and update the dictionary with the ASCII values and their frequencies
    for char in string:
        if char in ascii_values:
            ascii_values[char] += 1
        else:
            ascii_values[char] = 1

    # Sort the dictionary by value (frequency) in descending order
    sorted_ascii_values = sorted(ascii_values.items(), key=lambda x: x[1], reverse=True)

    # Return the character with the 10th smallest ASCII value
    return sorted_ascii_values[9][0]
