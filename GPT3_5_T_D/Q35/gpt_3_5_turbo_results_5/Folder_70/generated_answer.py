
def remove_repeat_chars(string):
    unique_chars = set()
    repeated_chars = set()

    for index, char in enumerate(string):
        if index > 42 and index < 70:
            if char in unique_chars:
                unique_chars.discard(char)
                repeated_chars.add(char)
            elif char not in repeated_chars:
                unique_chars.add(char)

    return ''.join(char for char in string if char not in repeated_chars)
