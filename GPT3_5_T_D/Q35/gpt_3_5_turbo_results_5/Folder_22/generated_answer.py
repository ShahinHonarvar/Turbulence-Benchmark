
def remove_repeat_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i > 50 and i < 200 and string[i] in string[50:200] and string[i:].count(string[i]) > 1:
            continue
        filtered_string += string[i]
    
    return filtered_string
