
def filter_chars(string):
    return "".join(char for index, char in enumerate(string) if not (41 <= index <= 64 and 'K' <= char <= ']'))
