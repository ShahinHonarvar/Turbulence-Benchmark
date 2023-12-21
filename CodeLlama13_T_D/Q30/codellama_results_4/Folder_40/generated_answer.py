
def insert_before_character(s):
    return "".join("e" + s[i-1] if s[i] == 'e' else s[i] for i in range(len(s)))
