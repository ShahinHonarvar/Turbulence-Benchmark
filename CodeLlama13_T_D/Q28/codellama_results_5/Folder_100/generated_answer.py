
def return_nth_smallest_ascii(string):
    chars = []
    for i in range(5, 48):
        if string[i] in chars:
            continue
        else:
            chars.append(string[i])
    
    sorted_chars = sorted(chars)
    return sorted_chars[12]
