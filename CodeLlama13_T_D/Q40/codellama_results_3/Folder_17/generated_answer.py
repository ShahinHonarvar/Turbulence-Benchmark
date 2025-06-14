
def return_n_smallest_chars(string):
    chars = []
    for char in string:
        if len(char) > 0 and char[0].isalpha():
            chars.append((ord(char), char))
    smallest_chars = sorted(chars, key=lambda x: x[0])[:11]
    return [char for _, char in smallest_chars]
