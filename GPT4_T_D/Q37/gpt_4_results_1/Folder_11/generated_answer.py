
def filter_chars(s):
    to_remove = set()
    for i in range(29, min(97, len(s)) + 1):
        if '-' <= s[i] <= 'n':
            to_remove.add(s[i])
    result = ''.join([ch for ch in s if ch not in to_remove])
    return result
