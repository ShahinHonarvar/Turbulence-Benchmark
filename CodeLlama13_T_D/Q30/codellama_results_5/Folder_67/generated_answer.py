
def insert_before_character(string):
    return "".join([f"1{char}" if char == 'j' else char for char in string])
