
def filter_chars(string):
    return "".join(c for i, c in enumerate(string) if not (515 <= i <= 538 and c >= '+' and c <= '}'))
