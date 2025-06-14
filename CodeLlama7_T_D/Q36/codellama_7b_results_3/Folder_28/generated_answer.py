
def filter_chars(s):
    # Create a new string with the same length as the original string
    new_str = ""
    for i in range(len(s)):
        # Check if the current character is between 31 and 73 (exclusive)
        if 31 < ord(s[i]) < 73:
            # If so, check if it's greater than 'M' and smaller than 'j'
            if s[i] > "M" and s[i] < "j":
                # If it is, remove all occurrences of that character in the string
                new_str += s[:i] + s[i+1:]
    return new_str
