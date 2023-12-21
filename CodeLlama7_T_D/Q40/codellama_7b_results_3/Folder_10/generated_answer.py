
def return_n_smallest_chars(string, n):
    # Create a dictionary to store the ASCII values of each character in the string
    ascii_values = {}
    for char in string:
        ascii_values[char] = ord(char)
    # Sort the dictionary by the ASCII values in descending order
    sorted_ascii_values = sorted(ascii_values.items(), key=lambda x: x[1], reverse=True)
    # Return the top 88 characters with the smallest ASCII values
    return [char for char, _ in sorted_ascii_values[:n]]
