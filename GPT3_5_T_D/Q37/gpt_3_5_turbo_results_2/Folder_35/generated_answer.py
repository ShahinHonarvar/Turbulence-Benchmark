
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 154 and i <= 402 and string[i] >= '(' and string[i] <= ']':
            continue
        filtered_string += string[i]
    return filtered_string
