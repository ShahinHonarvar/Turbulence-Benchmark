
def remove_repeat_chars(string):
    start = 0
    end = 5
    chars = set()
    result = ''
    
    for i, char in enumerate(string):
        if start < i < end:
            if char in chars:
                continue
            elif string.count(char, start, end) > 1:
                chars.add(char)
                continue
        
        result += char
    
    return result
