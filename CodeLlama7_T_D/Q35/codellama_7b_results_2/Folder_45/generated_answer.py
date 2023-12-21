
def remove_repeat_chars(s):
    # Split the string into characters
    chars = list(s)
    # Create a set to keep track of the unique characters
    unique_chars = set()
    # Loop through each character in the string
    for char in chars:
        # If the character is already in the set, remove all occurrences from the string
        if char in unique_chars:
            idx = 0
            while True:
                try:
                    del chars[idx]
                except IndexError:
                    break

                idx += 1

        # Otherwise, add the character to the set and continue with the next character
        else:
            unique_chars.add(char)

    # Join the characters back into a string
    new_string = "".join(chars)

    return new_string
