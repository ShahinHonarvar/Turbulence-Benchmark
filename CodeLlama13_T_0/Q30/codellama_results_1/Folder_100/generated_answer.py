
def insert_before_character(string):
    return "".join([f" {char}" if char == '0' else char for char in string])
