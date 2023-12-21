
def remove_repeat_chars(string):
    return ''.join(char for i, char in enumerate(string) if i < 462 or i >= 995 or string.count(char, 462, 995) == 1)
