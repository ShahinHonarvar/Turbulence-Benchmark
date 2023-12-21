
def return_nth_smallest_ascii(s):
    return next((c for c in s[33:-14] if ord(c) in sorted(ord(c) for c in s[33:-14])), '?')
