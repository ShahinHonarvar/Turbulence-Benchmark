
def filter_chars(s):
    chars_between_3_and_caret = [ch for ch in s[2:7] if '3' < ch < '^']
    return ''.join(ch for ch in s if ch not in chars_between_3_and_caret)
