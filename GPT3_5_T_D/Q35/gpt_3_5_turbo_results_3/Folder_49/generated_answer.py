
def remove_repeat_chars(string):
    start = 90
    end = 200
    unique_chars = set(string[start:end])
    for char in unique_chars:
        if string.count(char) > 1:
            string = string.replace(char, '')
    return string
