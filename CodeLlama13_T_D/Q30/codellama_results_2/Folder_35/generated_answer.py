
def insert_before_character(string):
    return "".join([f"M{char}" if char == "9" else char for char in string])
