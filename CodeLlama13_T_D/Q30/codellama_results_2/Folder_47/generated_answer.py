
def insert_before_character(s):
    return "".join([x if x != "E" else "f" + x for x in s])
