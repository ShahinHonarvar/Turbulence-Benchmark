
def return_nth_smallest_ascii(s):
    chars = []
    for i in range(40, 61):
        if s[i].isalpha():
            chars.append(ord(s[i]))
    return chr(sorted(chars)[18])
