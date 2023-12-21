
def insert_before_character(string, char):
    return ''.join([char + c if c == 'K' else c for c in string])
