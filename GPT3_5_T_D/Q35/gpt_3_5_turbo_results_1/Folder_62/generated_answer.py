
def remove_repeat_chars(string):
    return string[:50] + ''.join([ch for ch in string[50:92] if string[50:92].count(ch) == 1]) + string[92:]
