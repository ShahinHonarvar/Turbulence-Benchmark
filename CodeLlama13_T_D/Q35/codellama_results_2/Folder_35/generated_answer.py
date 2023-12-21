
def remove_repeat_chars(string):
    result = ""
    for i in range(77, 84):
        if string[i] != result[-1]:
            result += string[i]
    return result
