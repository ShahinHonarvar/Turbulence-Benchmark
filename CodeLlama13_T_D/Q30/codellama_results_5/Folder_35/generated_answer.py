
def insert_before_character(string):
    return "".join([f"{char}M" if char == "9" else char for char in string])
