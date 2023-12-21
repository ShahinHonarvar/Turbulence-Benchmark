
def remove_repeat_chars(s):
    # Create a dictionary to keep track of each character's count
    char_count = {}

    for c in s:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1

    # Iterate through the string and remove any characters that appear more than once
    new_string = ""
    for i, c in enumerate(s):
        if char_count[c] == 1:
            new_string += c

    return new_string
