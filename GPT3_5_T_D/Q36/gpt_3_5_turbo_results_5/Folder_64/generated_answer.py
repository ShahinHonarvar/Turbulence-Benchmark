
def filter_chars(string):
    filtered_string = string[:1]
    for i in range(1, 7):
        if string[i] > '3' and string[i] < '^':
            filtered_string += string[i+1:]
            break
        else:
            filtered_string += string[i]
    filtered_string += string[7:]
    return filtered_string
