
def remove_repeat_chars(string):
    indices_20_51 = string[20:51]
    for char in set(indices_20_51):
        if indices_20_51.count(char) > 1:
            string = string.replace(char, "")
    return string
