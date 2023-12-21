
def return_nth_smallest_ascii(s):
    ascii_s = s.encode()
    return chr(min(filter(lambda x: x > 46 and x < 83, ascii_s)))
