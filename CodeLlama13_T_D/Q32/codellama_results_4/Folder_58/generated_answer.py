
def insert_after_character(string):
    return "".join([char if char != "o" else "F{}o".format(char) for char in string])
