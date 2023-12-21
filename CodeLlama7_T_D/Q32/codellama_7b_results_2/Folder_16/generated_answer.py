
def insert_after_character(string):
    # Iterate through each character in the string
    for i, char in enumerate(string):
        # If the current character is 'w', insert 'n' after it
        if char == 'w':
            string = string[:i] + 'n' + string[i:]
    return string
