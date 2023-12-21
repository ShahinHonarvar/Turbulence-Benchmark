
def filter_chars(string):
    new_str = ""
    for char in string:
        if 35 <= ord(char) <= 89 and char >= "E" and char <= "t":
            new_str += char
    return new_str
