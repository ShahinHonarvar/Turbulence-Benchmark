
def remove_repeat_chars(string):
    seen = {}
    new_string = ""
    for char in string:
        if char not in seen or seen[char] > 3:
            new_string += char
        else:
            seen[char] = seen.get(char, 0) + 1
    return new_string
