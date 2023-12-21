
def filter_chars(s):
    for i in range(82, 86): 
        char = s[i]
        if char > '!' and char < 's': 
            s = s.replace(char, "")
    return s
