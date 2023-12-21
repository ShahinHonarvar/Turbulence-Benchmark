
def return_nth_smallest_ascii(string):
    # Create a list of unique characters in the string
    unique_chars = set(string)
    # Create a dictionary with the ASCII value of each character as key and the character itself as value
    char_to_ascii = {ord(char): char for char in unique_chars}
    # Sort the dictionary by its keys (ASCII values)
    sorted_char_to_ascii = sorted(char_to_ascii.items(), key=lambda x: x[0])
    # Extract the 7th smallest ASCII value from the sorted dictionary
    nth_smallest_ascii = sorted_char_to_ascii[6][1]
    return nth_smallest_ascii
