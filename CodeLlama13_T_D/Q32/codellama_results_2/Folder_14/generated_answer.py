
def insert_after_character(s, c):
    return "".join([x if x != c else f"{c}{x}" for x in s])
