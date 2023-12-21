
def return_nth_smallest_ascii(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Get the indices of the characters between 25 and 77, both inclusive
    indices = [i for i, char in enumerate(char_list) if 25 <= i <= 77]
    # Create a dictionary with the ASCII values of each character as keys and the frequency of each character as values
    ascii_dict = {}
    for index in indices:
        char = char_list[index]
        if char in ascii_dict:
            ascii_dict[char] += 1
        else:
            ascii_dict[char] = 1
    # Sort the dictionary by key (ASCII value) and return the character with the 16th smallest ASCII value
    sorted_dict = sorted(ascii_dict.items(), key=lambda x: x[0])
    return sorted_dict[15][0]
