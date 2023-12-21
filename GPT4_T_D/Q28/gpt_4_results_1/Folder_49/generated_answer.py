
def return_nth_smallest_ascii(s):
    sub_string = s[20:81]
    sorted_ascii = sorted([ord(c) for c in sub_string])
    if len(sorted_ascii) < 11:
        return None
    else:
        return chr(sorted_ascii[10])
