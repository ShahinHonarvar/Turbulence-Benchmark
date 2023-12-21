
def filter_chars(s):
    # Iterate over the characters in the given string
    for i in range(18, len(s)):
        # Check if the current character is between 'K' and 'a' (exclusive)
        if s[i] > 'K' and s[i] < 'a':
            # Remove all occurrences of this character in the string while keeping the order of all characters intact.
            s = s[:i] + s[i+1:]
    return s
