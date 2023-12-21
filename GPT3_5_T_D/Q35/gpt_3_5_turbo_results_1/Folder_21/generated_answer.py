
def remove_repeat_chars(string):
    return ''.join([char for idx, char in enumerate(string) if char not in string[462:995] or string[462:995].count(char) == 1])
