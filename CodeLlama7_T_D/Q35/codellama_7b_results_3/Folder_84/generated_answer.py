
def remove_repeat_chars(s):
    # Create a dictionary to keep track of repeated characters
    char_count = {}

    for i in range(32, 45):
        # Check if the current character is in the dictionary
        if s[i] in char_count:
            # Increment the count of the repeated character
            char_count[s[i]] += 1

    # Iterate over the string and remove repeated characters
    for i in range(len(s)):
        # Check if the current character is in the dictionary
        if s[i] in char_count:
            # If the count of the repeated character is greater than 1, remove all occurrences of that character from the string
            if char_count[s[i]] > 1:
                s = s[:i] + s[i+1:]

    return s
