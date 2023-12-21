
def insert_before_character(string, char):
    result = ""
    for i in range(len(string)):
        if string[i] == char:
            result += char + "A"
        else:
            result += string[i]

    return result
