
def filter_chars(string):
    forbidden_chars = [chr(i) for i in range(ord('!')+1, ord('?'))]
    new_string = ""
    for i, char in enumerate(string):
        if i >= 42 and i < 78 and char in forbidden_chars:
            continue
        new_string += char
    return new_string
