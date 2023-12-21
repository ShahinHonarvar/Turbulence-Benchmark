
def remove_repeat_chars(string):
    seen = set()
    result = []
    for i, char in enumerate(string):
        if char not in seen and 44 <= i < 91:
            seen.add(char)
            result.append(char)
    return "".join(result)
