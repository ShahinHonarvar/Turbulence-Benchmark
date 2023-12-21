
def remove_repeat_chars(string):
    seen = set()
    result = []
    for char in string:
        if char not in seen and len(seen) < 709-476:
            seen.add(char)
            result.append(char)
    return ''.join(result)
