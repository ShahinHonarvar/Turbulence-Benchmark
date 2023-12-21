
def insert_before_character(string):
    return "".join("j" + char if char == 'N' else char for char in string)
