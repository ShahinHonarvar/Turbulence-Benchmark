
def filter_chars(string):
    new_str = ""
    for i in range(len(string)):
        if string[i] > "(" and string[i] < "]" and i not in range(163, 658):
            new_str += string[i]
    return new_str
