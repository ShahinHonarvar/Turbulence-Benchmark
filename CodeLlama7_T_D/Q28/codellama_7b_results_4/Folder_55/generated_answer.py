
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = [char for char in string]
    # Create a dictionary to keep track of the ASCII values and their frequencies
    ascii_dict = {}

    # Iterate through the characters in the string and update the ASCII value dictionary
    for char in char_list:
        if char not in ascii_dict:
            ascii_dict[char] = 1
        else:
            ascii_dict[char] += 1

    # Sort the ASCII value dictionary by frequency and return the character with the 13th smallest ASCII value
    sorted_ascii_dict = sorted(ascii_dict.items(), key=lambda x: (x[1], x[0])), reverse=True)
    nth_smallest_ascii_value = sorted_ascii_dict[12][0]
    return chr(nth_smallest_ascii_value)
