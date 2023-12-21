
def remove_repeat_chars(string):
    return string[:80] + "".join([ch for ch in string[80:200] if string[80:200].count(ch) == 1]) + string[200:]
