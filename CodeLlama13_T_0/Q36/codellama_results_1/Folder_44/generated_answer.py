
def filter_chars(string):
    result = ""
    for i in range(len(string)):
        if i < 18 or i > 64:
            result += string[i]
        elif string[i] > "3" and string[i] < "B":
            continue
        else:
            result += string[i]
    return result
