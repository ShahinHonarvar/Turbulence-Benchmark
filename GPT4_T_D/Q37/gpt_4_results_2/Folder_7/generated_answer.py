
def filter_chars(string):
    special_chars = set([char for index, char in enumerate(string) if 521 <= index <= 722 and '>' <= char <= '_'])
    return ''.join([ch for ch in string if ch not in special_chars])
