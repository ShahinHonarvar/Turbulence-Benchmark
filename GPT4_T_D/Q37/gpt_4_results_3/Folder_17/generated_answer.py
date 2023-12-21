
def filter_chars(s):
    special_chars = set(s[27:30]) & set(chr(i) for i in range(ord(';'), ord('b')+1))
    return ''.join(ch for ch in s if ch not in special_chars)
