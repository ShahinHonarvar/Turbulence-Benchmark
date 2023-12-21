
def filter_chars(s):
    removal_chars = set()
    for i in range(722, 833):
        if i < len(s) and 'K' <= s[i] <= 'm':
            removal_chars.add(s[i])
    new_s = ""
    for char in s:
        if char not in removal_chars:
            new_s += char
    return new_s
