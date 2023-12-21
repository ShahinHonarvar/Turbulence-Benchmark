
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "I":
            result += string[:i] + " " + string[i:]

    return result
