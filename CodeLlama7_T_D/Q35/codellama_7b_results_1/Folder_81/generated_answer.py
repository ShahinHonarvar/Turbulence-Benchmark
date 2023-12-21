
def remove_repeat_chars(string):
    # Split the string into individual characters
    chars = list(string)

    # Iterate through each character in the string
    for char in chars:
        # Check if the current character is repeated between indices 20 and 200
        if chars.count(char) > 1 and len(chars) >= 20 and len(chars) <= 200:
            # Remove all occurrences of the repeated character from the string
            for i in range(len(chars)):
                if chars[i] == char:
                    del chars[i]
            break

    # Join the individual characters back into a string and return it
    return ''.join(chars)
