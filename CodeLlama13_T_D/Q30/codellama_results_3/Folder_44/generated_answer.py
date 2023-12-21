
def insert_before_character(string):
    return "".join("M" + char if char == 'g' else char for char in string)
