
def remove_repeat_chars(s):
    # Create a dictionary to keep track of characters
    char_dict = {}

    # Loop through the string and check if each character is already in the dictionary
    for i in range(len(s)):
        if s[i] not in char_dict:
            char_dict[s[i]] = 1

        else:

            # If the character is already in the dictionary, increment its count by 1
            char_dict[s[i]] += 1

    # Create a new string to store the altered characters
    new_str = ""

    # Loop through the characters of the original string and append them to the new string if they are not repeated
    for i in range(len(s)):
        if char_dict[s[i]] == 1:
            new_str += s[i]

    return new_str
