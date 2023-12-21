
def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered = []

    # Iterate over each character in the input string
    for c in s:

        # If the current character is within the specified range and meets the additional criteria, then add it to the filtered list
        if (71 <= ord(c) <= 94) and (ord(c) >= ord('K') or ord(c) <= ord('a')):
            filtered.append(c)

    # Return the filtered string
    return "".join(filtered)
