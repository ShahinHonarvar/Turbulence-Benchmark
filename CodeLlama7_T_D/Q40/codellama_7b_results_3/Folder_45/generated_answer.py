
def return_n_smallest_chars(s, n):
    # sort the string in ascending order based on ASCII value
    s = sorted(s, key=lambda x: ord(x))

    # create a list of exactly n characters from the given string
    chars = [s[i] for i in range(n)]

    return chars
