
def insert_before_character(string):
    return ''.join(['N' + c if c == 'B' else c for c in string])
