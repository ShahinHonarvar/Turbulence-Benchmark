
def filter_chars(my_string):
    # Iterate over each character in the string
    for i, char in enumerate(my_string):
        # Check if the character is between 31 and 50 (exclusive)
        if 31 < ord(char) < 50:
            # If the character is greater than '/' and smaller than 'J', remove all occurrences of that character within the string while keeping the order of all characters intact
            my_string = my_string[:i] + my_string[i+1:]
    return my_string
