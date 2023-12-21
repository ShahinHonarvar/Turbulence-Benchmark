
def remove_repeat_chars(s):
    temp = s[57:90]
    counts = {}
    for char in temp:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for char, count in counts.items():
        if count > 1:
            s = s.replace(char, '')
            
    return s
