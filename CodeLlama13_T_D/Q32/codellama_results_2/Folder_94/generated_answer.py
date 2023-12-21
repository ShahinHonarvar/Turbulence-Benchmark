
def insert_after_character(s, c):
    return "".join([f"{c}{s[i]}5" if s[i] == " " else f"{s[i]}" for i in range(len(s))])
