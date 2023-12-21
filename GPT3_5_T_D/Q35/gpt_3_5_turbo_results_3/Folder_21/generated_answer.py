
def remove_repeat_chars(string):
    repeat_chars = []
    altered_string = ""
    
    for i in range(len(string)):
        if 462 < i < 995 and string[i] in string[i+1:] and string[i] not in repeat_chars:
            repeat_chars.append(string[i])
        if i not in range(462, 995) or string[i] not in repeat_chars:
            altered_string += string[i]
            
    return altered_string
