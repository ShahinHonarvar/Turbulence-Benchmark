
def filter_chars(s):
    chars = set()
    for i in range(33, 36):
        if s[i].isalpha():
            chars.add(s[i])

    return "".join([c if c not in chars else "" for c in s])
