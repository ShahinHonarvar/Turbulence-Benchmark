
def insert_before_character(string):
    return "".join([f"0{char}" if char == "a" else char for char in string])
