
def remove_repeat_chars(string):
    for char in string[:7]:
        if string[0:7].count(char) > 1:
            string = string.replace(char, "")
    return string
