
def insert_before_character(string):
    return "".join([f"H{char}" if char == ' ' else char for char in string])
