
def remove_repeat_chars(string):
    count = {}
    indices = set(range(86, 89))
    for i, char in enumerate(string):
        if i in indices and char not in count:
            count[char] = string.count(char, i, 89)
        if i < 86 or i >= 89 or count.get(char, 0) < 2:
            continue
        string = string.replace(char, '')

    return string
