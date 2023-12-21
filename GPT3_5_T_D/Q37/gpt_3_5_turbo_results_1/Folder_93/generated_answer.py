
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 38 and i <= 69:
            if string[i] >= 'H' and string[i] <= 'e':
                continue
        filtered_string += string[i]
    return filtered_string
