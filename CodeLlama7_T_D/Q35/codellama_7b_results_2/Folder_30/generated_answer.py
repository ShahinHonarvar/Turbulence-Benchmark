
def remove_repeat_chars(s):
    # Create a dictionary to keep track of repeated characters
    char_dict = {}

    # Iterate through the string and check for repeated characters
    for i in range(len(s)):
        if s[i] not in char_dict:
            char_dict[s[i]] = 1
        else:
            char_dict[s[i]] += 1

    # Iterate through the string again and remove repeated characters
    new_string = ""
    for i in range(len(s)):
        if s[i] not in char_dict or char_dict[s[i]] == 1:
            new_string += s[i]

    # Return the altered string
    return new_string
