
def filter_chars(string):
    filtered = ""
    for i in range(len(string)):
        if i < 35 or i > 60:
            filtered += string[i]
        elif string[i] > "!" and string[i] < "B":
            filtered += string[i]
        else:
            continue
    return filtered
