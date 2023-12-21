
def remove_repeat_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 409 or i >= 502 or string[409:502].count(c) <= 1])
