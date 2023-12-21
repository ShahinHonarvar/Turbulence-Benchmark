
def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the input string
    for char in s:

        # If the current character is between 43 and 69 (both exclusive) and is greater than 'B' and smaller than 'r', remove all occurrences of this character from the input string
        if ((ord(char) > 42 and ord(char) < 70)) and char.isalpha():
            filtered_chars.append(char)
    return "".join(filtered_chars)
