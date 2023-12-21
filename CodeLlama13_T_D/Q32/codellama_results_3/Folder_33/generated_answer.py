
def insert_after_character(string, char):
    return "".join(char + string[i] if string[i] == 'a' else string[i] for i in range(len(string)))
