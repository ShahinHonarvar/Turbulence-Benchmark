
def remove_repeat_chars(string):
    unique_chars = set(string[43:70])
    for char in unique_chars:
        if string[43:70].count(char) > 1:
            string = string.replace(char, "")
    return string
