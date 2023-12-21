
def remove_repeat_chars(string):
    counts = {}
    for char in string[68:99]:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    result = ""
    for char in string:
        if char in counts and counts[char] > 1:
            continue
        result += char

    return result
