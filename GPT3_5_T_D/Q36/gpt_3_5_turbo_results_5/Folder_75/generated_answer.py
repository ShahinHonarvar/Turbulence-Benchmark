
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 46 or i >= 74 or ord(string[i]) <= ord('&') or ord(string[i]) >= ord('M'):
            filtered_string += string[i]
    
    return filtered_string
