
def insert_before_character(string):
    return "".join([f"h{char}" if char == "9" else char for char in string])
