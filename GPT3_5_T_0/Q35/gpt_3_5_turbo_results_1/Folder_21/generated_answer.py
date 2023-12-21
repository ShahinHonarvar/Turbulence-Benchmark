
def remove_repeat_chars(string):
    return string[:462] + ''.join([char for char in string[462:995] if string[462:995].count(char) == 1]) + string[995:]
