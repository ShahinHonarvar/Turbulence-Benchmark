
def remove_repeat_chars(string):
    repeated_chars = set()
    result = ""
    
    for idx, char in enumerate(string):
        if idx > 18 and idx < 32:
            if char in repeated_chars:
                continue
            if string.count(char) > 1:
                repeated_chars.add(char)
                continue
        result += char
    
    return result
