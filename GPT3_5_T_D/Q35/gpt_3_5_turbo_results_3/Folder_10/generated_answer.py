
def remove_repeat_chars(string):
    start_index = 36
    end_index = 54
    for char in string[start_index:end_index]:
        if string.count(char) > 1:
            string = string.replace(char, "")
    return string
