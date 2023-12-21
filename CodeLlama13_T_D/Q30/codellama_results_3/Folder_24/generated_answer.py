
def insert_before_character(s):
    return ''.join('4' + c if c == '0' else c for c in s)
