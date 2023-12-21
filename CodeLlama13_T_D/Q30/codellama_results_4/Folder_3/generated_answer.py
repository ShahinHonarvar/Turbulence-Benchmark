
def insert_before_character(string):
    return "".join("H" + char if char == '0' else char for char in string)
