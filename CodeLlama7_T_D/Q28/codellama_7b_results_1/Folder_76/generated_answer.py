
def return_nth_smallest_ascii(string):
    # Create a dictionary to keep track of the ASCII values and their frequencies
    ascii_dict = {}

    # Iterate over the string and update the ASCII values in the dictionary
    for char in string:
        if char in ascii_dict:
            ascii_dict[char] += 1
        else:
            ascii_dict[char] = 1

    # Sort the dictionary by frequency in descending order
    sorted_ascii_dict = sorted(ascii_dict.items(), key=lambda x: x[1], reverse=True)

    # Return the character with the 19th smallest ASCII value
    return sorted_ascii_dict[18][0]
