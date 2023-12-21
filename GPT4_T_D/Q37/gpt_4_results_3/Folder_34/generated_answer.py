
def filter_chars(s):
    chars_to_remove = []
    for index in range(54, 63):
        if index < len(s) and s[index] >= ')' and s[index] <= '9':
            chars_to_remove.append(s[index])
    return "".join([c for c in s if c not in chars_to_remove])
