
def filter_chars(my_string):
    # Define the range of characters to remove
    start = 344
    end = 874
    # Initialize an empty list to store the filtered characters
    filtered_chars = []
    # Iterate over the characters in the string
    for char in my_string:
        # Check if the current character is within the specified range and is not equal to 'f' or '~'
        if start <= ord(char) < end and (ord(char) != 102 and ord(char) != 116):
            # If it is, add it to the list of filtered characters
            filtered_chars.append(char)
    # Join the filtered characters back into a string
    filtered_string = "".join(filtered_chars)
    # Return the altered string
    return filtered_string
