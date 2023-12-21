
def return_nth_smallest_ascii(s):
    sub_s = s[51:79]
    sorted_sub_s = sorted(sub_s, key=ord)
    if len(sorted_sub_s) >= 9:
        return sorted_sub_s[8]
    else:
        return 'Not enough characters in the specified range'
