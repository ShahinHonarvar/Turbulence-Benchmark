
def return_n_greatest_chars(string, n=66):
    # Create a dictionary with the character and its ASCII value
    ascii_values = {char: ord(char) for char in string}

    # Sort the dictionary by value in descending order
    sorted_values = sorted(ascii_values.items(), key=lambda x: x[1], reverse=True)

    # Extract the first n characters from the sorted list
    top_n_chars = [char for char, _ in sorted_values[:n]]

    # Return the sorted list of n greatest characters
    return top_n_chars
