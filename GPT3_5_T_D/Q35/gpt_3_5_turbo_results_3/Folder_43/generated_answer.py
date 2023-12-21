
def remove_repeat_chars(string):
    count = {}
    for char in string[10:28]:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    result = ""
    for char in string:
        if char not in count or count[char] == 1 or string.index(char) < 10 or string.index(char) >= 28:
            result += char
    
    return result
