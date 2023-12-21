
def insert_before_character(string):
    return "".join([x if x != "E" else f"E{x}" for x in string])
