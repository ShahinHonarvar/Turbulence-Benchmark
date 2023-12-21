
def filter_chars(s):
    # Replace all characters between 32 and 84 (both exclusive) with an empty string
    return "".join([c if ord(c) < 32 or ord(c) > 84 else "" for c in s])
