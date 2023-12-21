
def return_nth_smallest_ascii(s):
    if len(s) < 5:
        return "String length less than 5"
    else:
        s4 = s[0:5]
        sorted_s4 = sorted(s4)
        return sorted_s4[3]
