
def remove_repeat_chars(s):
    # Create a new string that will be returned at the end
    new_str = ""
    # Iterate over each character in the original string
    for i, c in enumerate(s):
        # If the current character is not in the range of 50-200, or if it is the first occurrence of that character, add it to the new string
        if i < 50 or i > 200 or s.count(c) == 1:
            new_str += c
    # Return the altered string
    return new_str
