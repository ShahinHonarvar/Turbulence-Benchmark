
def remove_repeat_chars(string):
    count = {}
    for char in string[10:100]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    altered_string = ''
    for char in string:
        if char in count and count[char] > 1:
            continue
        altered_string += char
    
    return altered_string
