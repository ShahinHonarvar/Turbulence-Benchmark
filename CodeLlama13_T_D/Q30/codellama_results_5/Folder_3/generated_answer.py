
def insert_before_character(string):
    return "".join("H" + string[i] if string[i] == '0' else string[i] for i in range(len(string)))
