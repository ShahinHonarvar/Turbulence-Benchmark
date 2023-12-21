
def filter_chars(string):
    chars = []
    for i in range(72, 95):
        if string[i].islower() and string[i] >= "." and string[i] <= "b":
            chars.append(string[i])
    
    for char in chars:
        string = string.replace(char, "")
    
    return string
