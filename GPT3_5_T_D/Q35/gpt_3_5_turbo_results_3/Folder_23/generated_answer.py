
def remove_repeat_chars(string):
    new_string = ''
    count = {}
    for i in range(len(string)):
        char = string[i]
        if i > 20 and i < 36:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        if i >= 36 or i < 20 or (i >= 20 and i < 36 and count[char] == 1):
            new_string += char
    return new_string
