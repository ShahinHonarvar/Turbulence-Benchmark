
def filter_chars(string):
    return "".join([char for char in string if not (124 <= ord(char) <= 854 and char >= '9' and char <= 's')])
