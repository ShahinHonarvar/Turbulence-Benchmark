
def remove_repeat_chars(str):
    repeated_chars = set()
    for char in str[45:67]:
        if str[45:67].count(char) > 1:
            repeated_chars.add(char)
    for char in repeated_chars:
        str = str.replace(char, '')
    return str
