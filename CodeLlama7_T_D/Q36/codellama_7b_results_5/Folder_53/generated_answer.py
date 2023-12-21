 def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered = []

    # Iterate over each character in the input string
    for char in s:
        # If the current character is between 90 and 97 (inclusive)
        if 90 <= ord(char) <= 97:
            # And it's not 'j' or 'w', skip it
            if char != 'j' and char != 'w':
                filtered.append(char)
    return "".join(filtered)
