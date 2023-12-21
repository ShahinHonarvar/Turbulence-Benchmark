
def remove_repeat_chars(string):
    return string[:80] + ''.join([c for c in string[80:200] if string[80:200].count(c) == 1]) + string[200:]
