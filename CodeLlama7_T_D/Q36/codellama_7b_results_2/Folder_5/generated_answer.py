
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    result = ""

    # Iterate over each character in the input string
    for char in s:
        # If the current character is not between 55 and 66 (exclusive) or it is not greater than 'f' or smaller than '|', append it to the result string
        if not (55 < ord(char) < 66) or (ord(char) > ord('f')) or (ord(char) < ord('|')):
            result += char
    return result
