
def remove_repeat_chars(string):
    for char in string[:5]:
        if string[:5].count(char) > 1:
            string = string.replace(char, "")
    return string
