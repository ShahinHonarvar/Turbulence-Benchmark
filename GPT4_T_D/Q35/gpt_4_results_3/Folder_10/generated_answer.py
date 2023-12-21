
def remove_repeat_chars(s):
    repeated_chars = [char for char in s[37:54] if s[37:54].count(char) > 1]
    new_string = ''
    for char in s:
        if char not in repeated_chars:
            new_string += char
    return new_string
