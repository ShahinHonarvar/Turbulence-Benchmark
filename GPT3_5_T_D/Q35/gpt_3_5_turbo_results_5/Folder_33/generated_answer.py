
def remove_repeat_chars(string):
    repeated_chars = set()
    for i in range(126, 825):
        char = string[i]
        if string.count(char, 126, 825) > 1:
            repeated_chars.add(char)
    for char in repeated_chars:
        string = string.replace(char, "")
    return string
