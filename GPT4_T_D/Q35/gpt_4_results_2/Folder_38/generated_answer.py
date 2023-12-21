
def remove_repeat_chars(s):
    substring = s[37:85]
    repeat_chars = [char for char in substring if substring.count(char) > 1]
    output = ''
    for char in s:
        if char not in repeat_chars:
            output += char
    return output
