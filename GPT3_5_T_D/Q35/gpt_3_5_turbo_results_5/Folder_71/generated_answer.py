
def remove_repeat_chars(string):
    repeated_chars = set()
    count = {}
    for i in range(len(string)):
        if 20 < i < 35:
            count[string[i]] = count.get(string[i], 0) + 1
            if count[string[i]] > 1:
                repeated_chars.add(string[i])
    result = ''
    for char in string:
        if char not in repeated_chars:
            result += char
    return result
