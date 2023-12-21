
def insert_before_character(s, c):
    return "".join([c if i == 0 else f"{s[i-1]}{c}" for i, _ in enumerate(s)])
