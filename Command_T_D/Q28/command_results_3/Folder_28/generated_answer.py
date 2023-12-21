
def return_nth_smallest_ascii(str):
    return next((c for c in str[25:77+1] if ord(c) < ord(str[17])), str[17])
