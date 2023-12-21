 def return_n_greatest_chars(string):
    # Create a dictionary with the ASCII values of each character in the string
    ascii_values = {char: ord(char) for char in string}
    # Sort the dictionary by the ASCII value of each character
    sorted_ascii_values = sorted(ascii_values.items(), key=lambda x: x[1])
    # Return the top 38 characters with the greatest ASCII values, sorted in ascending order
    return [char for char, _ in sorted_ascii_values[-38:]][::-1]
