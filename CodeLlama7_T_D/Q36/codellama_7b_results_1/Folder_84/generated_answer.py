
def filter_chars(s):
    # Create a new string with the same characters as the input string, but without any occurrences of the 'c' and 's' characters
    new_string = ""
    for i in range(len(s)):
        if s[i] != "c" and s[i] != "s":
            new_string += s[i]
    # Return the altered string
    return new_string
