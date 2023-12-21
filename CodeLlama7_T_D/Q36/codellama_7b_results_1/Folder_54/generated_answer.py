
def filter_chars(string):
    # Create a new string with the characters between indices 18 and 38 removed
    new_string = string[:18] + string[38:]
    # Iterate over each character in the new string
    for i in range(18, len(new_string)):
        # Check if the current character is greater than ')' and smaller than 'P'
        if new_string[i] > ')' and new_string[i] < 'P':
            # Remove all occurrences of the current character in the new string
            new_string = new_string[:i] + new_string[i+1:]
    return new_string
