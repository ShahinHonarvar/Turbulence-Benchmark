
def remove_repeat_chars(string):
    repeated_chars = set()
    for char in string[45:90]:
        if string.count(char) > 1 and char not in repeated_chars:
            repeated_chars.add(char)
            string = string.replace(char, "")
    return string
