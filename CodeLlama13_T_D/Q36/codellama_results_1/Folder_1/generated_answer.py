
def filter_chars(string):
    filtered = ""
    for i, c in enumerate(string):
        if i < 69 or i > 87:
            filtered += c
        elif c > "#" and c < "L":
            continue
        else:
            filtered += c
    return filtered
