
def return_nth_smallest_ascii(s):
    if len(s) >= 73:
        chars = sorted(s[12:73])
        return chars[12]
    else:
        return "String length is less than 73"
