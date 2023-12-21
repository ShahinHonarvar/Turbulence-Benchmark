
def insert_before_character(s):
    return "".join([c + "0" if c == 'i' else c for c in s])
