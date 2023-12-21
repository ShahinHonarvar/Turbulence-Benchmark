
def remove_repeat_chars(string):
    repeated_chars = set()
    for i, char in enumerate(string[30:200]):
        if char in string[30+i+1:200]:
            repeated_chars.add(char)
    for char in repeated_chars:
        string = string.replace(char, "")
    return string
