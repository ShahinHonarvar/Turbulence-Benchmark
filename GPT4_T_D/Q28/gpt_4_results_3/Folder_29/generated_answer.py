
def return_nth_smallest_ascii(s):
    chars=list(sorted(s[5:11]))
    if len(chars)>=6:
        result=chars[5]
    else:
        result=None
    return result
