
def remove_repeat_chars(string):
    string_list = list(string)
    for i in range(10, 100):
        char = string_list[i]
        if string_list.count(char) > 1:
            string = string.replace(char, "")
    return string
