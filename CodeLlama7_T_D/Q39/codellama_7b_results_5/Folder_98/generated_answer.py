
def return_n_greatest_chars(string, n=68):
    # Create a dictionary with the character and its ASCII value
    ascii_values = {}
    for char in string:
        ascii_values[char] = ord(char)

    # Sort the dictionary by value (ASCII value) in descending order
    sorted_ascii_values = sorted(ascii_values.items(), key=lambda x: x[1], reverse=True)

    # Return the top n characters from the sorted list
    return [char for char, _ in sorted_ascii_values[:n]]
