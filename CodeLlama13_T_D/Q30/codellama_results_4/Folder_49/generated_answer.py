
def insert_before_character(string, char):
    return "".join([char + char if char in string else char for char in string])
