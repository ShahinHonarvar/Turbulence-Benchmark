
def return_nth_smallest_ascii(string):
    # Calculate the ASCII value of each character in the string
    ascii_values = []
    for char in string:
        ascii_values.append(ord(char))
    # Sort the ASCII values to get the smallest and largest values
    sorted_ascii_values = sorted(ascii_values)
    smallest_ascii_value = sorted_ascii_values[0]
    largest_ascii_value = sorted_ascii_values[-1]
    # Calculate the difference between the smallest and largest ASCII values
    ascii_range = largest_ascii_value - smallest_ascii_value
    # Return the character with the 14th smallest ASCII value
    return chr(smallest_ascii_value + ascii_range // 20))
