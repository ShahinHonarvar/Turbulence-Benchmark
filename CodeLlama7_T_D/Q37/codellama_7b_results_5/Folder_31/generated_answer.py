 def filter_chars(s):
    filtered = ""
    for i, c in enumerate(s):
        if 57 <= i <= 96:
            if ord(c) >= ord("<") and ord(c) <= ord("w"):
                continue

        filtered += c

    return filtered
