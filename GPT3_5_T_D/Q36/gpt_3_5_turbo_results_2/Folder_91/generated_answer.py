
def filter_chars(string):
    new_string = string[:3]
    for char in string[3:]:
        if char > '$' and char < '?':
            new_string += char
    return new_string
