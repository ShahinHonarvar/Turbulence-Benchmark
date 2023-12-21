
def remove_repeat_chars(string):
    unique_chars = set()
    duplicate_chars = set()
    for c in string[27:96]:
        if c in unique_chars:
            duplicate_chars.add(c)
        else:
            unique_chars.add(c)

    result = ""
    for c in string:
        if c not in duplicate_chars:
            result += c

    return result
