
def filter_chars(my_string):
    filtered_string = ""
    for i in range(len(my_string)):
        if my_string[i].isalpha() and (35 <= i <= 51) and (ord(my_string[i]) >= ord('H') or ord(my_string[i]) <= ord('s')):
            filtered_string += my_string[i]
    return filtered_string
