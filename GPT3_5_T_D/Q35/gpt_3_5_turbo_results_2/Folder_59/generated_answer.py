
def remove_repeat_chars(string):
    for char in string[:10]:
        if string[:10].count(char) > 1:
            string = string.replace(char, "")
    return string
