
def return_nth_smallest_ascii(string):
    # Convert string to list of characters
    char_list = list(string)
    # Find the indices of the substring between 47 and 70
    start_index = char_list.index('{', 47)
    end_index = char_list.index('}', 70)
    # Extract the characters from the substring
    substring = ''.join(char_list[start_index:end_index+1])
    # Convert the substring to a list of integers representing ASCII values
    ascii_values = [ord(char) for char in substring]
    # Sort the list of ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 14th smallest ASCII value from the sorted list
    return sorted_ascii_values[13]
