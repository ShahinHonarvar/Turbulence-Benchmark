
def remove_repeat_chars(string):
    count = {}
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char in count:
        if 1 < count[char] < 9:
            string = string.replace(char, '')

    return string
