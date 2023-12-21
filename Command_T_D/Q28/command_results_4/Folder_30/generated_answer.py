
def return_nth_smallest_ascii(s):
    ascii_list = sorted(set(s[50:-1]), key=lambda x: ord(x))[:11]
    return ascii_list[10]
