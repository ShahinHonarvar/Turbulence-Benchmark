
def filter_chars(my_string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the string
    for char in my_string:
        # Check if the current character is between the indices 163 and 658 (both exclusive)
        if ord(char) >= 163 and ord(char) < 658:
            # If it is, check if it is greater than '(' and smaller than ']'
            if char > '(' and char < ']':
                # If it is, skip this character in the filtered list
                continue

        # If the current character is not between the indices 163 and 658 (both exclusive) or if it is greater than '(' and smaller than ']', add it to the filtered list
        filtered_chars.append(char)

    # Join the filtered characters back into a string and return it
    return "".join(filtered_chars)
