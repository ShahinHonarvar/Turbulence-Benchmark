
def filter_chars(string):
    return "".join([char for i, char in enumerate(string) if not(88 <= i <= 90 and 'J' <= char <= 'Q')])
