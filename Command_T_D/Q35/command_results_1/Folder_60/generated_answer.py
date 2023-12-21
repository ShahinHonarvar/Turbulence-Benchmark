def remove_repeat_chars(str):
    for i in range(38, 52):
        if str[i] in str[:i]:
            str = str.replace(str[i], "")
    return str
