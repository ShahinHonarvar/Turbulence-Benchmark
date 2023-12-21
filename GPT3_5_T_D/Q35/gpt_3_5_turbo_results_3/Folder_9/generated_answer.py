
def remove_repeat_chars(string):
    repeated_chars = set()
    for char in string[80:200]:
        if string[80:200].count(char) > 1:
            repeated_chars.add(char)
    result = ''
    for char in string:
        if char not in repeated_chars:
            result += char
    return result
