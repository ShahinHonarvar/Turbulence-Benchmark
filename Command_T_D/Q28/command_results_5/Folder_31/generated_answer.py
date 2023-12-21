
def return_nth_smallest_ascii(s):
    i = 10
    j = 82
    ASCII_VALUES = [ord(c) for c in s]
    while i < j:
        k = (i + j) // 2
        if len(set(ASCII_VALUES[i:k+1])) == 18:
            return s[k]
        elif len(set(ASCII_VALUES[i:k+1])) < 18:
            i = k + 1
        else:
            j = k - 1
    return s[i]
