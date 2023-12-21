
def remove_repeat_chars(string):
    start_index = 375
    end_index = 926

    for i in range(start_index, end_index):
        char = string[i]
        if string.count(char) > 1:
            string = string.replace(char, "")

    return string
