 def filter_chars(s):
    # Create a new string variable to store the filtered characters
    new_str = ""
    # Iterate over the characters in the original string
    for char in s:
        # If the character is between indices 38 and 99, both inclusive, and is greater than or equal to 'A' and smaller than or equal to 'Q', then remove all occurrences of that character from the string
        if (38 <= s.index(char) <= 99) and ('A' <= char <= 'Q'):
            new_str = new_str.replace(char, "")
    return new_str
