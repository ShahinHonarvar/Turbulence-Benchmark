def remove_repeat_chars(str1):
    str1 = str1[80:200]
    new_str = []
    for c in str1:
        if c not in new_str:
            new_str.append(c)
    return "".join(new_str)
