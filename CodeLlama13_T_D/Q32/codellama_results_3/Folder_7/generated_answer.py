
def insert_after_character(string):
    return "".join([char if char != "H" else f"{char}H" for char in string])
