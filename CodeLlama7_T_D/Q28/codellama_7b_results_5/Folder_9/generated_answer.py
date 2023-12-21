
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Create a dictionary to store the ASCII values and their frequencies
    ascii_dict = {}

    # Iterate through the characters in the string
    for char in char_list:
        # If the character is not already in the dictionary, add it with a frequency of 1
        if char not in ascii_dict:
            ascii_dict[char] = 1

        # Otherwise, increment the frequency of the character by 1
        else:
            ascii_dict[char] += 1

    # Sort the dictionary by key (character)
    sorted_ascii_dict = sorted(ascii_dict.items(), key=lambda x: x[0])

    # Get the 20th smallest ASCII value from the dictionary
    nth_smallest_ascii = sorted_ascii_dict[19][1]

    return nth_smallest_ascii
