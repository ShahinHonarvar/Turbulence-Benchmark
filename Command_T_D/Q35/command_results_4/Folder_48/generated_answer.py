def remove_repeat_chars(str):
    i = 1
    while i < len(str) - 1:
        if str[i] in str[i + 1:]:
            str = str.replace(str[i], '').replace(str[i + 1], '').replace(str[i + 2], '').replace(str[i + 3], '')
            i += 1
        else:
            i += 1
    return str
