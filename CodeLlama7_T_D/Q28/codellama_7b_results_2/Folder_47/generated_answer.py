
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 3 and 52, both inclusive
    characters = string[3:52+1]
    # Create a list of tuples containing the character and its ASCII value
    char_asc_list = [(char, ord(char)) for char in characters]
    # Sort the list of tuples by the ASCII value in descending order
    sorted_list = sorted(char_asc_list, key=lambda x: x[1], reverse=True)
    # Return the 8th smallest ASCII value in the sorted list
    return sorted_list[7][0]
