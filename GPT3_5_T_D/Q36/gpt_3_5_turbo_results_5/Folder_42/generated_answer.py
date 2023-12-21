
def filter_chars(s):
    start = 42
    end = 68
    t = ord('t')
    x = ord('x')
    filtered_string = ""
    
    for i in range(len(s)):
        if i >= start and i < end and t < ord(s[i]) < x:
            continue
        filtered_string += s[i]
    
    return filtered_string
