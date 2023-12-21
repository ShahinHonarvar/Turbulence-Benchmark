
def return_nth_smallest_ascii(s):
    chars = []
    for i in range(12, 56):
        if s[i] != '':
            chars.append(ord(s[i]))
    return chr(sorted(chars)[16])
