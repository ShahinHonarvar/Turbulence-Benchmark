
def insert_before_character(string, character):
    return "".join([f"{character if i % 2 else ''}{char}" for i, char in enumerate(string)])
