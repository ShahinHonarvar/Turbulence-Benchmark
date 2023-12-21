
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "M":
            result += string[:i + 1] + "f"
        else:
            result += string[i]

    return result
