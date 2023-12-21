
def remove_repeat_chars(string):
    repeat_chars = set()
    
    for char in string[57:84]:
        if string.count(char) > 1:
            repeat_chars.add(char)
    
    for char in repeat_chars:
        string = string.replace(char, "")
    
    return string
