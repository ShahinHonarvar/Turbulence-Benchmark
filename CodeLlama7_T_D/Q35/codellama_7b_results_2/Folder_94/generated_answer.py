
def remove_repeat_chars(s):
    # Create a dictionary to keep track of characters
    char_dict = {}

    # Iterate over the string and update the dictionary
    for i in range(len(s)):
        if s[i] not in char_dict:
            char_dict[s[i]] = 1

        else:
            char_dict[s[i]] += 1

    # Iterate over the dictionary and remove repeated characters from the string
    for key, value in char_dict.items():
        if value > 1:
            s = s.replace(key, '', 1)

    return s
