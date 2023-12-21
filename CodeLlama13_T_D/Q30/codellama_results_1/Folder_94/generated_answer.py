
def insert_before_character(string):
    return "".join([c if c != " " else f"5{c}" for c in string])
