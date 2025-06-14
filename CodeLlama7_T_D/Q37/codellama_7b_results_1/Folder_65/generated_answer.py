
def filter_chars(s):
    # Create a new string with the same length as the original string
    new_string = ""

    # Iterate over each character in the original string
    for c in s:
        if 61 <= ord(c) <= 70 and ord(c) >= ord('0') and ord(c) <= ord('@'):
            # If the current character is within the specified range, remove it from the new string
            continue

        else:

            # Otherwise, add the current character to the new string
            new_string += c

    return new_string
