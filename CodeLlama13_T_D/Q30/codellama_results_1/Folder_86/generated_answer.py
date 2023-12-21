
def insert_before_character(string):
    return "".join("Q" + char if char == 'O' else char for char in string)
