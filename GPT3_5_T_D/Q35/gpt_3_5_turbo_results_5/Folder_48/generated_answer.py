
def remove_repeat_chars(string):
    repeat_chars = set()
    for c in string[409:502]:
        if string[409:502].count(c) > 1:
            repeat_chars.add(c)
    altered_string = ''.join([c for c in string if c not in repeat_chars])
    return altered_string
