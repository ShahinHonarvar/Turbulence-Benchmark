
def insert_before_character(s):
    return "".join("m" + s[i:] if s[i] == 'F' else s[i] for i in range(len(s)))
