 def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered = []

    # Iterate over each character in the input string
    for c in s:
        # If the current character is between indices 33 and 70, both inclusive, and is greater than or equal to character '7' and smaller than or equal to character 'k', then append it to the filtered list
        if (33 <= ord(c) <= 70) and ('7' <= c <= 'k'):
            filtered.append(c)

    # Join the filtered characters back into a string and return it
    return "".join(filtered)
