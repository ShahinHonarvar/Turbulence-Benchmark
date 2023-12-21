
def filter_chars(string):
    # Remove all occurrences of characters between indices 28 and 65, both inclusive, that are greater than or equal to character 'O' and smaller than or equal to character 'd'.
    for i in range(28, 66):
        if string[i] >= "O" and string[i] <= "d":
            string = string.replace(string[i], "")
    return string
