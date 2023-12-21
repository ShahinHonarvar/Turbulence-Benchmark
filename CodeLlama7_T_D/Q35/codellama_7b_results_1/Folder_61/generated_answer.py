
def remove_repeat_chars(s):
    # Create a dictionary to keep track of characters
    char_dict = {}

    # Iterate through the string and update the dictionary
    for i in range(len(s)):
        if s[i] not in char_dict:
            char_dict[s[i]] = 1

        else:

            char_dict[s[i]] += 1


    # Iterate through the dictionary and remove all characters that occur more than once
    for i in range(len(char_dict)):

        if char_dict[i] > 1:

            s = s.replace(str(i), '', char_dict[i])

    return s
