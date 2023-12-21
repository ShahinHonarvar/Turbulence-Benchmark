
def remove_repeat_chars(string):
    indices = set()
    for i in range(200, 202):
        if string[i] in string[i+1:]:
            indices.add(i)
    
    result = ''
    for i, char in enumerate(string):
        if i not in indices:
            result += char
    
    return result
