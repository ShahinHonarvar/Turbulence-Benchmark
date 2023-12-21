
def insert_before_character(string):
    return "".join("Z" + char if char == "C" else char for char in string)
