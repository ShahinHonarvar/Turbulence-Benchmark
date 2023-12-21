
def remove_repeat_chars(string):
    unique_chars = set()
    for i in range(20, 43):
        char = string[i]
        if char not in unique_chars and string.count(char) > 1:
            unique_chars.add(char)
            string = string.replace(char, "")
    return string
