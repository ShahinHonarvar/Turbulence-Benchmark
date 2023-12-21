
def return_n_smallest_chars(string, n=44):
    # Create a list of tuples containing the ASCII value and character
    ascii_list = [(ord(char), char) for char in string]
    # Sort the list by ASCII value in ascending order
    sorted_list = sorted(ascii_list, key=lambda x: x[0])
    # Return the top n characters from the sorted list
    return [x[1] for x in sorted_list[:n]]
