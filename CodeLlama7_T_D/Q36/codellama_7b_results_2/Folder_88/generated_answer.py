
def filter_chars(my_string):
    # Define the range of characters to remove
    start = 78
    end = 81
    # Initialize an empty list to store the filtered characters
    filtered_chars = []
    # Iterate over each character in the string
    for char in my_string:
        # If the current character is within the specified range and is not equal to 'S' or '[', add it to the filtered list
        if start <= ord(char) < end and char != "S" and char != "[":
            filtered_chars.append(char)
    # Join the filtered characters back into a string
    filtered_string = "".join(filtered_chars)
    return filtered_string
