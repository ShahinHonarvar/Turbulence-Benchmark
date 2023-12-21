
def return_n_smallest_chars(s):
    chars = sorted([chr(i) for i in range(256)], key=lambda x: ord(x))
    return ''.join(chars[:85])
