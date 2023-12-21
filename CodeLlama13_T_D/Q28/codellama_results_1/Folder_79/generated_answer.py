
def return_nth_smallest_ascii(s):
    chars = set()
    for i in range(13, 36):
        if s[i].isalpha():
            chars.add(ord(s[i]))
    return chr(sorted(chars)[17])
