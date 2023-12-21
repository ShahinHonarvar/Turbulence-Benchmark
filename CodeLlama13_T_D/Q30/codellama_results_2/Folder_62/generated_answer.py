
def insert_before_character(s, c):
    return "".join(f"{c}" if i == 0 else f"{s[i - 1]}{c}" for i, s in enumerate(s))
