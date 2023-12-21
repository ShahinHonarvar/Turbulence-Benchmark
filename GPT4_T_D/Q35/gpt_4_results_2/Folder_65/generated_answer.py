
def remove_repeat_chars(s):
    indices_51_76 = s[52:76]
    repeat_chars = [char for char in indices_51_76 if indices_51_76.count(char) > 1]
    return ''.join(char for char in s if char not in repeat_chars)
