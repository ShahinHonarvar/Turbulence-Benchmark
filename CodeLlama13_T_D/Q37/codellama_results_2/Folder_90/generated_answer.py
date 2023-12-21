
def filter_chars(s):
    return "".join([c for c in s if not (348 <= ord(c) <= 852 and 'J' <= c <= 'b')])
