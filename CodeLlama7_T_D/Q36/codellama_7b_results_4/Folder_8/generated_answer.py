
def filter_chars(string):
    result = ""
    for i in range(len(string)):
        if string[i] == '!':
            continue

        elif string[i] == '*':
            break

        else:
            result += string[i]

    return result
