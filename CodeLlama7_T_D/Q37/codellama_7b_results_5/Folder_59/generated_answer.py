 def filter_chars(string):
    filtered = ""
    for i in range(len(string)):
        if (i >= 2 and i <= 3) and (ord(string[i]) >= ord('5') and ord(string[i]) <= ord('_')):
            continue
        else:
            filtered += string[i]
    return filtered
