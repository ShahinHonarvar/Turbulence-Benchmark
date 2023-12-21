
def filter_chars(my_string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []
    # Iterate through each character in the string
    for char in my_string:
        # Check if the current character is within the specified range and meets the condition
        if 35 <= ord(char) <= 51 and ord('H') <= ord(char) <= ord('s'):
            # If so, add the character to the filtered characters list
            filtered_chars.append(char)
    # Join the filtered characters back into a string
    filtered_string = ''.join(filtered_chars)
    return filtered_string
