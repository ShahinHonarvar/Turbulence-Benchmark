
def remove_repeat_chars(string):
    repeat_chars = set()
    for i in range(70, 98):
        char = string[i]
        if char in string[70:98] and string.count(char) > 1:
            repeat_chars.add(char)
    for char in repeat_chars:
        string = string.replace(char, "")
    return string
