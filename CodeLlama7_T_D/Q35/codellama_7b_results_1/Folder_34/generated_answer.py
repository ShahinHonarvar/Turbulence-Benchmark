
def remove_repeat_chars(s):
    # Create a dictionary to keep track of repeated characters
    char_count = {}

    for i in range(len(s)):
        # Update the count of each character in the string
        if s[i] not in char_count:
            char_count[s[i]] = 1
        else:
            char_count[s[i]] += 1

    # Create a new string with all repeated characters removed
    new_string = ""

    for i in range(len(s)):

        if char_count[s[i]] == 1:
            new_string += s[i]

    return new_string
