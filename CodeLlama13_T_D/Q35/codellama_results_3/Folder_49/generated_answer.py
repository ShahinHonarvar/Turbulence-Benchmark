
def remove_repeat_chars(s):
    seen = set()
    return "".join([c for c in s if ord(c) < 90 or ord(c) > 200 and not (ord(c) in seen or seen.add(ord(c)))])
