
def insert_before_character(s, c):
    return "".join([f"{c}d" if x == c else x for x in s])
