
def insert_before_character(s, c):
    return "".join([f"{c}u" if x == "t" else x for x in s])
