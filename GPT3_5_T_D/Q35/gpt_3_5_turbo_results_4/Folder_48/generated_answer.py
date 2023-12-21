
def remove_repeat_chars(string):
    return string[:409] + ''.join([x for i, x in enumerate(string[409:502], 409) if string[409:502].count(x) == 1]) + string[502:]
