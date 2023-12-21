
def filter_chars(s):
    # Get the indices of the characters between 54 and 92
    start = ord('5') - 1
    end = ord('X') + 1
    # Initialize an empty string to store the filtered characters
    filtered = ''

    for i in range(len(s)):
        # Check if the current character is between 54 and 92 (exclusive)
        if start <= ord(s[i]) <= end:
            # If it is, skip over all occurrences of that character within the string
            while i < len(s) and s[i] == s[i + 1]:
                i += 1

        else:
            filtered += s[i]

    return filtered
