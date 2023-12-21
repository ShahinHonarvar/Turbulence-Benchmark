
def remove_repeat_chars(string):
    seen = {}
    for i in range(36, 85):
        if string[i] in seen:
            del seen[string[i]]
        else:
            seen[string[i]] = True
    
    result = ""
    for i in range(len(string)):
        if i not in seen:
            result += string[i]
    
    return result
