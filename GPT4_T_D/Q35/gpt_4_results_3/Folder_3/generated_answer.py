
def remove_repeat_chars(string):
    target = string[57:88]
    for ch in target:
        if target.count(ch) > 1:
            string = string.replace(ch, "")
    return string
