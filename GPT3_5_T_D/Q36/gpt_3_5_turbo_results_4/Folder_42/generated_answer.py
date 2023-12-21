
def filter_chars(string):
    start = 42
    end = 68
    t = ord('t')
    x = ord('x')
    
    chars = list(string)
    filtered = []
    
    for i in range(len(chars)):
        if start <= i < end and t < ord(chars[i]) < x:
            continue
        filtered.append(chars[i])
    
    return ''.join(filtered)
