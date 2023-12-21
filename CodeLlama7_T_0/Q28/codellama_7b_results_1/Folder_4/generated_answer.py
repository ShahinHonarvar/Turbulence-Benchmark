
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Create a dictionary to store the ASCII values of each character
    ascii_dict = {}
    # Loop through each character in the string and add its ASCII value to the dictionary
    for char in char_list:
        ascii_dict[char] = ord(char)
    # Sort the dictionary by the ASCII value of each character
    sorted_dict = sorted(ascii_dict.items(), key=lambda x: x[1])
    # Return the 4th smallest ASCII value in the sorted dictionary
    return sorted_dict[3][0]
