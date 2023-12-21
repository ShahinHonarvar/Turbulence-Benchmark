
def return_nth_smallest_ascii(str):
    return next((x for x in str[36:79+1] if ord(x) < ord(str[11])), str[36])
