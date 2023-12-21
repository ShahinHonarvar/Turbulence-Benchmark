
def insert_after_character(s):
    return "".join([i if i != "j" else f"{i}q" for i in s])
