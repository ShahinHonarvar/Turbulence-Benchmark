
def remove_repeat_chars(string):
    for character in set(string[25:80]):
        if string.count(character) > 1:
            string = string.replace(character, "")
    return string
