
def return_n_smallest_chars(string):
    # Create a dictionary to store the ASCII values and characters of the given string
    ascii_dict = {char: ord(char) for char in string}
    # Sort the dictionary by the ASCII value in ascending order
    sorted_ascii_dict = sorted(ascii_dict.items(), key=lambda x: x[1])
    # Create a list of the smallest 45 characters based on the sorted dictionary
    smallest_chars = [char for char, ascii_val in sorted_ascii_dict[:45]]
    return smallest_chars
