
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 21 or i >= 25 or string[i] <= '5' or string[i] >= '}':
            filtered_string += string[i]
    return filtered_string
