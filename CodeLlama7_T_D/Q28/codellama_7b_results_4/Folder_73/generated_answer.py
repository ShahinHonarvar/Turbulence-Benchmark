
def return_nth_smallest_ascii(string):
    # Get the characters that occur between indices 0 to 69, both inclusive
    chars = string[0:70]
    # Create a list of tuples containing (ASCII value, character) for each character in the string
    ascii_list = [(ord(char), char) for char in chars]
    # Sort the list by ASCII value in descending order
    sorted_list = sorted(ascii_list, key=lambda x: x[0], reverse=True)
    # Return the 10th smallest ASCII value and its corresponding character
    return sorted_list[9][1]
