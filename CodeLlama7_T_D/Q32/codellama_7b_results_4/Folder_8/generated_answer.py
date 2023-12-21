
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "E":
            result += "TE"
        else:
            result += string[i]
    return result
