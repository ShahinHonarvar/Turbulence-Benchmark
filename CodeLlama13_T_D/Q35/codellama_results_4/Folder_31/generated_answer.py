
def remove_repeat_chars(string):
    result = ""
    for i in range(33, 78):
        if string[i] not in result:
            result += string[i]
    return result
