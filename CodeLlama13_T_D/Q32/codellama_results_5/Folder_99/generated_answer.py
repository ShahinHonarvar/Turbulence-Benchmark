
def insert_after_character(s):
    return "".join([char if char != "W" else "aW" for char in s])
