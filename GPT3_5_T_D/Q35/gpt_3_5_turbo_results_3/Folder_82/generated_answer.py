
def remove_repeat_chars(string):
    count = {}
    for char in string[30:200]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    result = ''
    for char in string:
        if char in count and count[char] > 1:
            continue
        result += char
    
    return result
