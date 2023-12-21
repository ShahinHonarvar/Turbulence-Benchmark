import re
def return_n_greatest_chars(s):
    if not isinstance(s, str):
        raise ValueError("First argument must be a string")
    if len(s) < 47:
        return s
    greatest_chars = re.findall(r"[A-Z][^A-Z]*", s)[-47:]
    return "".join(sorted(greatest_chars, key=lambda c: ord(c), reverse=True))
