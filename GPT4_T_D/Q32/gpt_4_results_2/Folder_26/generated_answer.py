
def insert_after_character(s):
    s_new = ""
    for i in s:
        if i == 'r':
            s_new += "rw"
        else:
            s_new += i
    return s_new
