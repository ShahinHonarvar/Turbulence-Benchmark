
def return_nth_smallest_ascii(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Create a dictionary to store the ASCII values and their corresponding indices

    ascii_dict = {}

    for i, char in enumerate(char_list):
        ascii_value = ord(char)

        if ascii_value not in ascii_dict:
            ascii_dict[ascii_value] = []

        ascii_dict[ascii_value].append(i)

    # Get the 19th smallest ASCII value from the dictionary

    sorted_values = sorted(ascii_dict.keys())

    nth_smallest = sorted_values[18]

    # Return the character with the 19th smallest ASCII value at index 58 to 85, both inclusive

    return char_list[ascii_dict[nth_smallest][0]]
