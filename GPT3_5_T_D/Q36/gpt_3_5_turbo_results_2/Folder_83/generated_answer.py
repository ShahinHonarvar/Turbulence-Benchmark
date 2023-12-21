
def filter_chars(string):
    filtered = ""
    for i in range(len(string)):
        if i < 72 or i >= 93:
            filtered += string[i]
        elif string[i] > '<' and string[i] < 'J':
            filtered = filtered.replace(string[i], "")
    return filtered
