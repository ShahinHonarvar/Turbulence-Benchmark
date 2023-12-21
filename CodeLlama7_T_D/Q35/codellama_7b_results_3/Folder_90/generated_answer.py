
def remove_repeat_chars(s):
    # Create a dictionary to keep track of each character's count
    char_count = {}
    # Iterate through the string and increment the count for each character
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    # Iterate through the dictionary and remove all characters with a count greater than 1
    for c in char_count:
        if char_count[c] > 1:
            s = s.replace(c, '')
    return s
