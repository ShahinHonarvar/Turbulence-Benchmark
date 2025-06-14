
def remove_repeat_chars(s):
    # create a dictionary to keep track of characters
    char_count = {}

    # iterate over the string and count the number of occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # create a new string with only unique characters
    new_s = ""

    # iterate over the dictionary and append each character to the new string
    for char, count in char_count.items():
        if count == 1:
            new_s += char

    return new_s
