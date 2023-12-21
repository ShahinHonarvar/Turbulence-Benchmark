
def filter_chars(my_string):
    filtered_string = ""
    for i in range(46, 85+1):
        if my_string[i].isalpha():
            if my_string[i] >= '-' and my_string[i] <= 'X':
                continue

        filtered_string += my_string[i]
    return filtered_string
