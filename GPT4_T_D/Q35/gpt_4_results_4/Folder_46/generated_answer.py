
def remove_repeat_chars(string):
    str_interval = string[11:79]
    remove_chars = [char for char in str_interval if str_interval.count(char) > 1]
    
    for ch in remove_chars:
        string = string.replace(ch, "")

    return string
