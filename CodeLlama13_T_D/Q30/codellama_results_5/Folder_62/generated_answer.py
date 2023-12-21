
def insert_before_character(s):
    return "".join([c if c != " " else f"o{c}" for c in s])
