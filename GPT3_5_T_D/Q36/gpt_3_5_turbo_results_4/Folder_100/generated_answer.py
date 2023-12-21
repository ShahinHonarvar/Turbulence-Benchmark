 
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 43 <= i < 69:
            if 'B' < string[i] < 'r':
                continue
        filtered_string += string[i]
    return filtered_string
