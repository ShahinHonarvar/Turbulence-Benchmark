
def insert_before_character(string, character):
    return "".join([f"{char}W" if char == " " else char for char in string])
