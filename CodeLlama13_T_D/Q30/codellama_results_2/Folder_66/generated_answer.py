
def insert_before_character(string, k):
    return "".join([f"{k if c == 'k' else ''}{c}" for c in string])
