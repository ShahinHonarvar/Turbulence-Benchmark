
def return_nth_smallest_ascii(string):
    # Get the characters between indices 30 and 70
    sub_string = string[30:71]
    # Create a dictionary to store the ASCII values of the characters
    ascii_dict = {}
    # Iterate over the characters in the substring
    for char in sub_string:
        # Get the ASCII value of the character
        ascii_val = ord(char)
        # If the ASCII value is not already present in the dictionary, add it to the dictionary with a count of 1
        if ascii_val not in ascii_dict:
            ascii_dict[ascii_val] = 1
        # Otherwise, increment the count of the ASCII value by 1
        else:
            ascii_dict[ascii_val] += 1
    # Get the keys (ASCII values) of the dictionary and sort them in ascending order
    sorted_keys = sorted(ascii_dict.keys())

    # Return the character with the 15th smallest ASCII value among those characters that occur between indices 30 to 70, both inclusive.
    return chr(sorted_keys[14])
