
def filter_chars(s):
    removed_chars=set(s[i] for i in range(36, 41) if 'H'<=s[i]<='e')
    return ''.join(ch for ch in s if ch not in removed_chars)
