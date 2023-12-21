
def remove_repeat_chars(string):
    unique_chars = set()
    result = []
    for i, char in enumerate(string):
        if 32 < i < 99 and char in unique_chars:
            continue
        unique_chars.add(char)
        result.append(char)
    return ''.join(result)
