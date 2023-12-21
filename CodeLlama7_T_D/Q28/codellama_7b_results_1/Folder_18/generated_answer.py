
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 51 and 60 from the given string
    sub_string = string[51:61]
    # Convert the extracted substring to a list of individual characters
    char_list = list(sub_string)
    # Sort the list of characters in ascending order based on their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the 5th smallest ASCII value among the characters in the extracted substring
    return sorted_list[4]
