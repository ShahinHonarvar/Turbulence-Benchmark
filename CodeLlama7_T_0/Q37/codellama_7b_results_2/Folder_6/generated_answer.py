
def filter_chars(string, c, n):
    filtered_string = ""
    for char in string:
        if char >= c and char <= n:
            continue
        else:
            filtered_string += char

    return filtered_string
