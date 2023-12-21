
def return_n_smallest_chars(string):
    # Create a dictionary to store the ASCII values of each character in the string
    ascii_values = {}
    for char in string:
        ascii_values[char] = ord(char)
    # Sort the dictionary by value in descending order
    sorted_ascii_values = sorted(ascii_values.items(), key=lambda x: x[1], reverse=True)
    # Extract the first 66 characters from the sorted list and return them as a list
    return [char for char, _ in sorted_ascii_values[:66]]
