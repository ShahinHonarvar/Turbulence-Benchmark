
def insert_after_character(string):
    return "".join([c if c != 'N' else f"{c}z" for c in string])
