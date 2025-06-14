
def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered = []

    # Iterate over each character in the string
    for char in s:
        # If the current character is between indices 34 and 67, both inclusive, and is greater than or equal to 'W' and smaller than or equal to 'x', append it to the filtered list
        if (char >= 'W') and (char <= 'x') and ((s.index(char) + 1) > 34) and ((s.index(char) + 1) < 67):
            filtered.append(char)
    # Join the filtered characters together into a string
    s = "".join(filtered)

    # Return the altered string
    return s
