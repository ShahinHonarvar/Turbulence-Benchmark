
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between 44 and 69 (both inclusive)
    start = string.index('<') + 1
    end = string.rindex('>') - 1
    # Initialize a list to store the ASCII values of the characters in the string between the indices 44 and 69
    ascii_values = []
    for i in range(start, end + 1):
        ascii_values.append(ord(string[i]))
    # Sort the list of ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the character with the 15th smallest ASCII value among those characters in the string between the indices 44 and 69
    return chr(sorted_ascii_values[15])
