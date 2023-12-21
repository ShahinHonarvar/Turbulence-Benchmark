
def return_n_greatest_chars(s):
    s = list(set(s))
    s.sort(reverse=False, key=lambda char: ord(char))
    return s[-49:]
