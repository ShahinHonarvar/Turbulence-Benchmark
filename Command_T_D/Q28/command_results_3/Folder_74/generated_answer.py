
def return_nth_smallest_ascii(s):
    return next((c for c in s[1:32] if ord(c) in range(ord(s[0])+1, ord(s[0])+32)), s[0])
