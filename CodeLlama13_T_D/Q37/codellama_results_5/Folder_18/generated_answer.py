
def filter_chars(s):
    return "".join([c for c in s if not (770 <= ord(c) <= 970 and ord('-') <= ord(c) <= ord('D'))])
