
def insert_before_character(string, char):
    return ''.join('u' + c if c == char else c for c in string)
