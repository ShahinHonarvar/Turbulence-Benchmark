
def remove_repeat_chars(string):
    # Create a dictionary to keep track of character occurrences
    char_count = {}

    # Iterate through the string and increment the count for each character
    for char in string:
        if char not in char_count:
            char_count[char] = 1

        else:
            char_count[char] += 1

    # Iterate through the dictionary and remove all characters that occur more than once
    for char, count in char_count.items():
        if count > 1:
            string = string.replace(char, '')

    return string
