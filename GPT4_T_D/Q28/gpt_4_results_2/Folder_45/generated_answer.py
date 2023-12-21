
def return_nth_smallest_ascii(s):
    trimmed_str = s[0:16]
    asciis = [ord(x) for x in trimmed_str]
    asciis.sort()
    return chr(asciis[15])
