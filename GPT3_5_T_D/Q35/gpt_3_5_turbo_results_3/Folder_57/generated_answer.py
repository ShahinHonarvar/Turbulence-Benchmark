
def remove_repeat_chars(string):
    repeated_chars = set()

    for i in range(25, 80):
        char = string[i]
        if char in string[25:80] and char not in repeated_chars:
            repeated_chars.add(char)
            string = string.replace(char, '')

    return string
