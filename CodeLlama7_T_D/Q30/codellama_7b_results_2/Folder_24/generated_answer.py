
def insert_before_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "0":
            result += "4"

        result += string[i]

    return result
