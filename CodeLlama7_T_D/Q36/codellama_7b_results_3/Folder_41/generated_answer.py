 def filter_chars(s):
    # Initialize a list to store the filtered characters
    filtered_chars = []
    # Iterate over the characters in the string
    for char in s:
        # Check if the character is between indices 81 and 89 (both exclusive)
        if 80 < ord(char) < 91:
            # If the character is greater than 'f' and smaller than '{', remove all occurrences of that character from the string while keeping the order of all characters intact.
            filtered_chars.append(char)
    # Join the filtered characters into a single string and return it.
    return "".join(filtered_chars)
