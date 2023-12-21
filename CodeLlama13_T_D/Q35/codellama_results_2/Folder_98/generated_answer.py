
def remove_repeat_chars(string):
    char_count = {}
    for i in range(7):
        if string[i] in char_count:
            char_count[string[i]] += 1
        else:
            char_count[string[i]] = 1
    
    for i in range(7):
        if char_count[string[i]] > 1:
            string = string.replace(string[i], "")
    
    return string
