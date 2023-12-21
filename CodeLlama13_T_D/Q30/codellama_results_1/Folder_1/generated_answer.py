
def insert_before_character(string, char):
    return "".join([f"{char if c == 'U' else ''}T{c}" for c in string])
