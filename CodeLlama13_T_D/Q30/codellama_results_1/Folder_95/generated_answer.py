
def insert_before_character(s, c):
    return "".join([f"q{i}" if i == c else i for i in s])
