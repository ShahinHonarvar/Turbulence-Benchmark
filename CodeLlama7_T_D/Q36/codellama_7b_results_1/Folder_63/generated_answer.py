
def filter_chars(string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []
    # Iterate through each character in the string
    for char in string:
        # If the current character is greater than '<' and smaller than '>', remove all occurrences of that character within the string
        if char > '<' and char < '>':
            filtered_chars.append(char)
    # Join the filtered characters to form a new string
    return "".join(filtered_chars)
