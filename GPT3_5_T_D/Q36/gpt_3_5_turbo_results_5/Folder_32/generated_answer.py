
def filter_chars(string):
    new_string = string[:40]
    for char in string[40:63]:
        if char > '7' and char < 'H':
            new_string = new_string.replace(char, "")
    new_string += string[63:]
    return new_string
