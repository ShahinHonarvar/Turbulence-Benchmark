
def remove_repeat_chars(string):
    return string[:50] + ''.join([c for i, c in enumerate(string[50:92]) if string[50:92].count(c) <= 1]) + string[92:]
