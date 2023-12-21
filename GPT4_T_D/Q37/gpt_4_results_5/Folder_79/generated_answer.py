
def filter_chars(s):
    filtered_chars = [char for char in s[10:53] if char >= '@' and char <= 'T']
    filtered_string = ""
    for i in s:
        if i not in filtered_chars:
            filtered_string += i
    return filtered_string
