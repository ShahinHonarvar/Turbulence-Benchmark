
def filter_chars(s):
    # Define the range of characters to remove
    start = ord('(') + 1
    end = ord('O') - 1
    # Create a new string with the removed characters
    result = ''
    for char in s:
        if not (start <= ord(char) < end):
            result += char

    return result
