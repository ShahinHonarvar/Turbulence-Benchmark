
def insert_after_character(s):
    return ''.join(c if c != 'm' else 'F' + c for c in s)
