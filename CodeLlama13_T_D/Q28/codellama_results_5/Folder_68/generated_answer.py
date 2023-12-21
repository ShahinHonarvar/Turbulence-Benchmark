
def return_nth_smallest_ascii(s):
    return min([c for c in s[0:11] if c in ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'])
