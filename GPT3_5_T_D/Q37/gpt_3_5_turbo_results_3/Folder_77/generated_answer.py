
def filter_chars(string):
    return "".join([c for i, c in enumerate(string) if not (384 <= i <= 411 and '/' <= c <= '8')])
