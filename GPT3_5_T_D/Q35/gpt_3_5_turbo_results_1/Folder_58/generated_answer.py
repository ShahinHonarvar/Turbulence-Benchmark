
def remove_repeat_chars(string):
    start = 103
    end = 802
    unique_chars = set(string[start:end])
    for char in unique_chars:
        if string[start:end].count(char) > 1:
            string = string.replace(char, '')
    return string
